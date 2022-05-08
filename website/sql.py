import sqlite3
from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from flask_login import current_user
from werkzeug.security import generate_password_hash, check_password_hash
from website import db
from flask_login import login_user, login_required, logout_user, current_user
import json

try:
    sqliteConnection = sqlite3.connect('database.db')
    cursor = sqliteConnection.cursor()
    print("Database created and Successfully Connected to SQLite")

    number = db.session.query("SELECT COUNT(first_name) FROM whosin;")
    db.session.commit()
    print(number)
     

except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)
