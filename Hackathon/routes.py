from flask import render_template, url_for, flash, redirect, request, abort
from Hackathon import app

@app.route("/home")
@app.route("/")
def home():
	return render_template('index.html')

@app.route("/login")
def login():
	return render_template('login.html')

@app.route("/signup")
def signup():
	return render_template('signup.html')