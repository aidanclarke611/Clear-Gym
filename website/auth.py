from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from flask_login import current_user
from .models import Admin, Note, User, whosin
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
import json

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist', category='error')
    
    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
         
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 4 characters.', category='error')
        elif len(first_name) < 2:
            flash('First Name must be greater than 2 characters.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created!', category='success')
            return redirect(url_for('auth.login'))
            
    return render_template("sign_up.html", user=current_user)


@auth.route('/forum', methods=['GET', 'POST'])
def forum():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Comment is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Comment added!', category='success')

    return render_template("forum.html", user=current_user)

@auth.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
     
    return render_template("forum.html", user=current_user)

@auth.route('/about')
@login_required
def about():

    return render_template("about.html", user=current_user)


@auth.route('/store')

def store():
    return render_template("store.html", user=current_user)

@auth.route('/cart')

def cart():
    return render_template("cart.html", user=current_user)

@auth.route('/checkout')

def checkout():
    return render_template("checkout.html", user=current_user)

@auth.route('/jack')
@login_required
def jack():
    return render_template("Trainers/jack.html", user=current_user)

@auth.route('/katie')
@login_required
def katie():
    return render_template("Trainers/katie.html", user=current_user)

@auth.route('/daniel')
@login_required
def daniel():
    return render_template("Trainers/daniel.html", user=current_user)


@auth.route('/adminhome')
def adminhome():
    return render_template("adminhome.html", user=current_user)

@auth.route('/whos_in')
def whos_in():
    return render_template("whos_in.html", user=current_user)



@auth.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        note = request.form.get('note')

       
    new_note = whosin(first_name=current_user.first_name, user_id=current_user.id)        
    db.session.add(new_note)
    db.session.commit()
    flash('Signed in successfully!', category='success')

    return render_template("whos_in.html", user=current_user)


@auth.route('/whos_in', methods=['POST'])
def whoisin():
  
    number = db.session.query("SELECT COUNT(user_id) FROM whosin;")
    db.session.commit()
    print(number)
     

    return render_template("whos_in.html", user=current_user)

@auth.route('/whosin_table')
def whosin_table():
    return render_template("whosin_table.php", user=current_user)
    

@auth.route('/adminlogin', methods=['GET', 'POST'])
def adminlogin():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        admin = Admin.query.filter_by(email=email).first()
        if admin:
            if password == admin.password:
                flash('Logged in successfully!', category='success')
                login_user(admin, remember=True)
                return redirect(url_for('auth.adminhome'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist', category='error')
    
    return render_template("adminlogin.html", user=current_user)


@auth.route('/adminlogout')
def logoutadmin():
    logout()
    return redirect(url_for('auth.adminlogin'))


@auth.route('/view_delete')
def view_delete():
    return render_template("view_delete.html", user=current_user)

@auth.route('/adminsign-up', methods=['GET', 'POST'])
def adminsign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
         
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 4 characters.', category='error')
        elif len(first_name) < 2:
            flash('First Name must be greater than 2 characters.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created!', category='success')
            return redirect(url_for('auth.adminhome'))
            
    return render_template("adminsign-up.html", user=current_user)


@auth.route('/trial')
def trial():
    return render_template("trial.html", user=current_user)


@auth.route('/signout', methods=['POST'])
def delete_ID():
    id = json.loads(request.data)
    user_id = id['user_id']
    id = Note.query.get(user_id)
    if id:
        if id.user_id == current_user.id:
            db.session.delete(user_id)
            db.session.commit()
     
    return render_template("whos_in.html", user=current_user)


@auth.route('/dumbbell')

def dumbbell():
    return render_template("items/dumbbell.html", user=current_user)


@auth.route('/bench')

def bench():
    return render_template("items/bench.html", user=current_user)


@auth.route('/barbell')

def barbell():
    return render_template("items/barbell.html", user=current_user)


@auth.route('/kettle')

def kettle():
    return render_template("items/kettle.html", user=current_user)

@auth.route('/foam')

def foam():
    return render_template("items/foam.html", user=current_user)


@auth.route('/band')

def band():
    return render_template("items/band.html", user=current_user)





  



