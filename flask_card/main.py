from flask import Blueprint, render_template
from flask_login import login_required
from . import db

main = Blueprint('main', __name__)

@main.route('/')
@login_required
def index():
    return render_template("landing.html")

@main.route('/profile')
@login_required
def profile():
    return render_template("profile.html")