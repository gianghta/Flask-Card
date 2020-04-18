from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from .. import db
from ..models import Collection
from . import main
from .form import FlashcardCollectionForm


@main.route('/', methods=['GET', 'POST'])
def index():
    if not current_user.is_authenticated:
        return render_template("landing.html")
    form = FlashcardCollectionForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            name = form.name.data
            category = form.category.data
            collection = Collection.query.filter_by(name=name).first()
            if not collection:
                collection = Collection(name=form.name.data, category=form.name.data)
                collection.user = current_user
                db.session.add(collection)
                db.session.commit()
                flash('Flashcard Collection added.')
                return redirect(url_for('main.index'))
            flash('Flask collection is already existed!')
            return redirect(url_for('main.index'))
    collection = current_user.collections.order_by(Collection.timestamp.desc()).all()
    if collection:
        return render_template("dashboard.html", user=current_user, form=form, collection=collection)
    return render_template("dashboard.html", user=current_user, form=form, collection=[])

@main.route('/profile')
@login_required
def profile():
    return render_template("profile.html", user=current_user)

@main.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "public, max-age=0, must-revalidate"
    return r