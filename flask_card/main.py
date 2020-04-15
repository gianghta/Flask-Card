from flask import Blueprint, render_template
from flask_login import login_required, current_user
from . import db
from .models import User

main = Blueprint('main', __name__)

@main.route('/')
def index():
    if not current_user.is_authenticated:
        return render_template("landing.html")
    return render_template("dashboard.html", user=current_user)

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