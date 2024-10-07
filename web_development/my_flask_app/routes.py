from flask import render_template, redirect, url_for, flash
from app import app, db
from forms import RegistrationForm, LoginForm
from models import User
from flask_bcrypt import Bcrypt

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check email and password.', 'danger')
    return render_template('login.html', form=form)


@app.route('/')
def home():
    items = ["Javascript", "Python", "SQL", "CSS"]
    return render_template('home.html', title="Home Page", name="Fidel", items=items)

@app.route('/greet', methods=['POST'])
def greet():
    username = request.form['username']
    return render_template('greet.html', title="Greeting Page", username=username)


@app.route('/about')
def about():
    return render_template('about.html', title="About Page")
