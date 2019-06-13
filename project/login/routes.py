# The idea for the login functionality was taken from: https://www.youtube.com/watch?v=vVx1737auSE
from project import mongo
from flask import Flask, render_template, request, session, flash, redirect, url_for, Blueprint 
from flask_pymongo import pymongo
import bcrypt

login_function = Blueprint('login_function', __name__)

#Login page
@login_function.route("/login")
def login():
    return render_template('login.html')

#Send login data to the database   
@login_function.route('/login_form', methods=['POST'])
def login_form():
    users = mongo.db.users
    login_user = users.find_one({'name' : request.form['username']})
    
    if login_user:
        if bcrypt.hashpw(request.form['password'].encode('utf-8'), login_user['password']) == login_user['password']:
            session['username'] = request.form['username']
            flash("You are logged in")
        return redirect(url_for('homepage.index'))
    return 'Invalid username or password'
    
#Add a new user to the database    
@login_function.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name' : request.form['username']})
        
        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
            users.insert({'name' : request.form['username'], 'password' : hashpass})
            session['username'] = request.form['username']
            flash("Your account has benn created")
            return redirect(url_for('homepage.index'))
        return 'That username already exists!'
    return render_template("register.html")

#Logout
@login_function.route('/logout')
def logout():
    session.clear()
    flash("You have been logged out successfully")
    return redirect(url_for('homepage.welcome'))
