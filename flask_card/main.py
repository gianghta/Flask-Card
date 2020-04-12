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