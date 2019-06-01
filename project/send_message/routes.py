from flask import Flask, render_template, request, flash, redirect, url_for, Blueprint
from flask_mail import Mail, Message
from project import mail

mail_function = Blueprint('mail_function', __name__)

@mail_function.route("/mailto",methods=['POST', 'GET'])
def mailto():
    return render_template("mailto.html", page_title="Send a message") 
    

@mail_function.route('/send_mail', methods=['POST', 'GET'])
def send_mail():
    message = request.form['message']
    email = request.form['email']
    name = request.form['name']
    msg = Message(subject = """Message sent by  """ +str(name), sender=name , recipients=["flaskmail123@gmail.com"])
    msg.html = str(message) +"""<br>You can reply to """ +str(email)
    mail.send(msg)
    flash("We've recived your message")
    return redirect(url_for('mail_function.mailto'))