import os, math, re
from flask import Flask, render_template, request, session, flash, redirect, url_for, jsonify, json
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId
from pymongo import MongoClient
import json
from bson import json_util
from bson.json_util import dumps
from flask_compress import Compress
import bcrypt
from flask_mail import Mail, Message
from config import Config
    
app = Flask(__name__)
app.config.from_object(Config)
Compress(app)

mail = Mail(app)
mongo = PyMongo(app)

from project.login.routes import login_function
from project.send_message.routes import mail_function
from project.statistics.routes import statistics_function
from project.recipes.routes import all_recipes
from project.cuisines.routes import all_cuisines
from project.homepage.routes import homepage

app.register_blueprint(login_function)
app.register_blueprint(mail_function) 
app.register_blueprint(statistics_function)
app.register_blueprint(all_recipes)
app.register_blueprint(all_cuisines)
app.register_blueprint(homepage)

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True
        )
