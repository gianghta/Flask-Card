from flask import Blueprint, render_template
from flask_login import login_required
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template("landing.html")

@main.route('/dashboard')
@login_required
def dashboard():
    return render_template("dashboard.html")

@main.route('/profile')
@login_required
def profile():
    return render_template("profile.html")