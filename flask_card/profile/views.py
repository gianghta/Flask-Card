from flask import render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from . import profile


@profile.route("/profile")
@login_required
def profile_page():
    return render_template("profile.html", user=current_user)

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
