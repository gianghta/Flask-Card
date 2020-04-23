from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from .. import db
from ..models import Collection, Category
from . import main
from .form import FlashcardCollectionForm, FlashcardCollectionEditForm, FlashcardForm


@main.route("/", methods=["GET", "POST"])
def index():
    if not current_user.is_authenticated:
        return render_template("landing.html")
    form = FlashcardCollectionForm()
    if request.method == "POST":
        if form.validate_on_submit():
            name = form.name.data
            category_data = form.category.data
            description = form.description.data
            category = Category.query.filter_by(name=category_data).first()
            collection = Collection.query.filter_by(name=name).first()
            if not category:
                category = Category(name=category_data)
                category.user = current_user
                db.session.add(category)
                db.session.commit()
                flash("New category created.")

            if not collection:
                collection = Collection(name=name, description=description)
                collection.user = current_user
                collection.category = category
                db.session.add(collection)
                db.session.commit()
                flash("Flashcard Collection added.")
                return redirect(url_for("main.index"))
            flash("Flask collection is already existed!")
            return redirect(url_for("main.index"))
    collection = current_user.collections.order_by(Collection.timestamp.desc()).all()
    category = current_user.category.order_by(Category.id.desc()).all()
    if collection and category:
        return render_template(
            "dashboard.html",
            user=current_user,
            form=form,
            collection=collection,
            category=category,
        )
    if category:
        return render_template(
            "dashboard.html",
            user=current_user,
            form=form,
            collection=[],
            category=category,
        )
    return render_template(
        "dashboard.html", user=current_user, form=form, collection=[], category=[]
    )


@main.route("/<int:id>/edit", methods=["GET", "POST"])
@login_required
def edit_collection(id):
    collection = Collection.query.get_or_404(id)
    form = FlashcardCollectionEditForm()
    if form.validate_on_submit():
        name = form.name.data
        description = form.description.data
        collection.name = name
        collection.description = description
        db.session.commit()
        return redirect(url_for("main.index"))
    return render_template("collection_edit.html", form=form)


@main.route("/<int:id>/delete", methods=["GET", "POST"])
@login_required
def delete_collection(id):
    collection = Collection.query.get_or_404(id)
    db.session.delete(collection)
    db.session.commit()
    return redirect(url_for("main.index"))

@main.route("/category/<int:id>/delete", methods=["GET", "POST"])
@login_required
def delete_category(id):
    category = Category.query.get_or_404(id)
    db.session.delete(category)
    db.session.commit()
    return redirect(url_for("main.index"))

@main.route("/flashcard/<name>")
@login_required
def flashcard_dashboard(name):
    form = FlashcardForm()
    collection = Collection.query.filter_by(name=name).first()
    return render_template("flashcardboard.html", form=form)

@main.route("/profile")
@login_required
def profile():
    return render_template("profile.html", user=current_user)


@main.after_request
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
