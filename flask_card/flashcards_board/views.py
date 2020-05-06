from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import login_required
from .. import db
from ..models import Collection, Flashcard
from . import flashcards_board
from .form import FlashcardForm, FlashcardEditForm
import json


@flashcards_board.route("/<name>/flashcard", methods=["GET", "POST"])
@login_required
def flashcard_dashboard(name):
    form = FlashcardForm()
    collection = Collection.query.filter_by(name=name).first()
    flashcard_collection = Flashcard.query.filter_by(collection_id=collection.id).all()

    if form.validate_on_submit():
        question = form.question.data
        answer = form.answer.data
        input_type = form.input_type.data
        flashcard = Flashcard.query.filter_by(question=question, answer=answer, input_type=input_type).first()

        if not flashcard:
            flashcard = Flashcard(question=question, answer=answer, input_type=input_type)
            flashcard.collection = collection
            db.session.add(flashcard)
            db.session.commit()
            flash("Flashcard added.")
            return redirect(url_for("flashcards_board.flashcard_dashboard", name=collection.name))

    return render_template(
        "/flashcard/flashcardboard.html",
        form=form,
        collection=collection,
        flashcard_collection=flashcard_collection
    )

@flashcards_board.route("/<name>/flashcard/<int:id>/edit", methods=["GET", "POST"])
@login_required
def edit_flashcard(name, id):
    collection = Collection.query.filter_by(name=name).first()
    flashcard = Flashcard.query.get_or_404(id)
    form = FlashcardEditForm()
    if form.validate_on_submit():
        flashcard.question = form.question.data
        flashcard.answer = form.answer.data
        flashcard.input_type = form.input_type.data
        db.session.commit()
        return redirect(url_for("flashcards_board.flashcard_dashboard", name=collection.name))
    return render_template("/flashcard/flashcard_edit.html", form=form, flashcard=flashcard)



@flashcards_board.route("/<name>/flashcard/delete/<int:id>", methods=["GET", "POST"])
@login_required
def delete_flashcard(name, id):
    flashcard = Flashcard.query.get_or_404(id)
    db.session.delete(flashcard)
    db.session.commit()
    return redirect(url_for("flashcards_board.flashcard_dashboard", name=name))


@flashcards_board.route("/<name>/flashcard/preview")
@login_required
def flashcard_preview(name):
    collection = Collection.query.filter_by(name=name).first()
    flashcard_collection = Flashcard.query.filter_by(collection_id=collection.id).all()

    flashcards = [row2dict(row) for row in flashcard_collection]

    return render_template(
        "/flashcard/flashcard_showcase.html",
        collection=collection,
        flashcards=json.dumps(flashcards),
    )


def row2dict(row):
    """
    Helper method that convert sqlalchemy base class into dictionary
    to import to front end JS script for JSON conversion
    """
    d = {}
    for column in row.__table__.columns:
        d[column.name] = str(getattr(row, column.name))
    return d

@flashcards_board.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers["Cache-Control"] = "public, max-age=0"
    return r
