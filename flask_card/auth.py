from flask import Blueprint, render_template, request, redirect, flash, url_for
from flask_login import login_required, login_user, logout_user, current_user
from .forms import SignupForm, LoginForm
from .models import User
from . import db, login_manager

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            email = form.get('email')
            password = form.get('password')
            user = User.query.filter_by(email=email).first()
            if user and user.check_password(password=password):
                login_user(user)
                next_page = request.args.get('next')
                return redirect(next_page or url_for('main.index'))
        flash('Invalid username/password combination')
        return redirect(url_for('auth.login'))
    
    return render_template("login.html", form=form)

@auth.route('/logout')
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('auth.login'))

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    """
    User sign-up page

    GET: Serve up sign-up form
    POST: If credentials submitted is valid, redirected to logged-in homepage
    """

    form = SignupForm()
    if request.method == 'POST':
        # User sign-up logic
        if form.validate_on_submit():
            name = form.get('name')
            email = form.get('email')
            password = form.get('password')
            existing_user = User.query.filter_by(email=email).first()
            if existing_user is None:
                user = User(email=email, username=name, password=password)
                db.session.add(user)
                db.session.commit()
                login_user(user)
                return redirect(url_for('main.index'))
            flash('A user already existed with that email address')
            return redirect(url_for('auth.signup'))

    return render_template("signup.html", form=form)

@login_manager.user_loader
def load_user(user_id):
    """Check if user is logged-in on every page load."""
    if user_id is not None:
        return User.query.get(user_id)
    return None


@login_manager.unauthorized_handler
def unauthorized():
    """Redirect unauthorized users to Login page."""
    flash('You must be logged in to view that page.')
    return redirect(url_for('auth.login'))