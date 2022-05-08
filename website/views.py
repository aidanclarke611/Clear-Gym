from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from . models import Note
from . import db
import json
from django.shortcuts import render
from.models import whosin

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    return render_template("home.html", user=current_user)

@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})


def index(request):
    if request.method=='POST':
        id = request.POST['type']
        first_name = request.POST['name']

        obj = whosin()
        obj.id = id
        obj.first_name = first_name
        obj.save()


    from django.core import serializers
    data = serializers.serialize("python", whosin.objects.all())

    context = {
    'data' :data,
    }


    return render(request, 'whosin.html', context)


