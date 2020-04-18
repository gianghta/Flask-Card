from flask import Blueprint, render_template
from flask_login import login_required, current_user
from .. import db
from ..models import User, Collection
from . import main
from .form import FlashcardCollectionForm


@main.route('/')
def index():
    if not current_user.is_authenticated:
        return render_template("landing.html")
    return render_template("dashboard.html", user=current_user)

@main.route('/profile')
@login_required
def profile():
    return render_template("profile.html", user=current_user)

@main.route('/add-collection', methods=['GET', 'POST'])
@login_required
def add_collection():
    form = FlashcardCollectionForm()
    if form.validate_on_submit():
        collection = Collection(name=form.name.data, category=form.name.data)
        collection.user = current_user
        db.session.add()
        db.session.commit()
        flash('Flashcard Collection added.')
        return redirect(url_for('main.index'))
    return render_template('main.index', form=form)

@main.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "public, max-age=0, must-revalidate"
    return r