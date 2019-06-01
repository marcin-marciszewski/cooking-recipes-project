from project import mongo
from flask import Flask, render_template, request, session, flash, redirect, url_for, Blueprint
import bcrypt

login_function = Blueprint('login_function', __name__)

@login_function.route("/login")
def login():
    return render_template('login.html')

    
@login_function.route('/login_form', methods=['POST'])
def login_form():
    users = mongo.db.users
    login_user = users.find_one({'name' : request.form['username']})
    
    if login_user:
        if bcrypt.hashpw(request.form['pass'].encode('utf-8'), login_user['password']) == login_user['password']:
            session['username'] = request.form['username']
            flash("You're logged in")
        return redirect(url_for('homepage.index'))
    return 'Invalid username or password'
    
    
@login_function.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name' : request.form['username']})
        
        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())
            users.insert({'name' : request.form['username'], 'password' : hashpass})
            session['username'] = request.form['username']
            flash("Your account has benn created")
            return redirect(url_for('homepage.index'))
        return 'That username already exists!'
    return render_template("register.html")


@login_function.route('/logout')
def logout():
    session.clear()
    flash("You've been logged out successfully")
    return redirect(url_for('homepage.index'))
