from flask import render_template, url_for, flash, redirect, request, abort
from Hackathon import app, bcrypt, db, mail
from Hackathon.forms import RegisterationForm, LoginForm, RequestResetForm, ResetPasswordForm
from Hackathon.models import User, ParkingLot
from flask_login import login_user, current_user, logout_user, login_required
from flask_mail import Message

@app.route("/home")
@app.route("/")
def home():
	return render_template('index.html')

@app.route("/logout")
def logout():
	logout_user()
	return redirect(url_for('login'))

@app.route("/booking")
def booking():
	return render_template('booking.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return render_template('index.html')
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user and bcrypt.check_password_hash(user.password, form.password.data):
			login_user(user)
			return render_template('index.html')
		else:
			flash('Login Unsuccessful, Please check your email and password', 'danger')
	return render_template('login.html', form=form)

@app.route("/signup", methods=['GET', 'POST'])
def signup():
	if current_user.is_authenticated:
		return render_template('index.html')
	form = RegisterationForm()
	form2 = LoginForm()
	if form.validate_on_submit():
		hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user = User(email=form.email.data, password=hashed_password, company=form.company.data)
		db.session.add(user)
		db.session.commit()
		flash('Your Account Has Been Successfully Created. Now you can Log In', 'success')
		return render_template('login.html', form=form2)
	return render_template('signup.html', form=form)