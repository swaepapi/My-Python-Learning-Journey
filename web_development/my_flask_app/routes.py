from flask import render_template, redirect, url_for, flash
from app import app, db
from forms import  LoginForm
from models import User
from flask_bcrypt import Bcrypt
from flask import request, session
from forms import SignupForm
from flask import session, redirect, url_for, flash
from functools import wraps
from flask_login import login_user, logout_user, login_required



@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            flash('That email is already taken. Please choose a different one.', 'danger')
        else:
            new_user = User(email=form.email.data, password=form.password.data)
            db.session.add(new_user)
            db.session.commit()
            flash('Your account has been created! You can now log in.', 'success')
            return redirect(url_for('login'))
    return render_template('signup.html', form=form)







@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.password == form.password.data:  # Add password hashing later for security
            session['user_id'] = user.id  # Set user session
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', form=form)


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please log in to access this page', 'warning')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out!', 'info')
    return redirect(url_for('login'))

# @app.route('/')
# def home():
#     items = ["Javascript", "Python", "SQL", "CSS"]
#     return render_template('home.html', title="Home Page", name="Fidel", items=items)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/home')
@login_required
def home():
    # Example: check if the user is logged in via session
    if 'user_id' not in session:
        flash('Please log in to access this page.', 'warning')
        return redirect(url_for('login'))
    
    return render_template('home.html')


@app.route('/greet', methods=['POST'])
def greet():
    username = request.form['username']
    return render_template('greet.html', title="Greeting Page", username=username)


@app.route('/about')
def about():
    return render_template('about.html', title="About Page")
