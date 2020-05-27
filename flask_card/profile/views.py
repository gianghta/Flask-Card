from flask import render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from ..models import User
from . import profile
from .form import ChangeProfileForm
from .. import db


@profile.route("/profile")
@login_required
def profile_page():
    return render_template("/profile/profile.html", user=current_user)


@profile.route("/profile/edit", methods=["GET", "POST"])
@login_required
def edit_profile_page():
    form = ChangeProfileForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data

        current_user.username = name
        current_user.email = email
        current_user.password = password
        db.session.commit()
        flash("User account is updated!")
        return redirect(url_for("profile.edit_profile_page"))
    return render_template("/profile/edit_profile.html", user=current_user, form=form)


@profile.after_request
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
