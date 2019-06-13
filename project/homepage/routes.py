from flask import Flask, render_template, request, flash, session, redirect, url_for, Blueprint, make_response
from flask_pymongo import pymongo
from project import mongo
from functools import wraps
from project import auth_required

homepage = Blueprint('homepage', __name__)

@homepage.route("/")
def welcome():
    if session:
        session.clear()
    return render_template("welcome.html")

@homepage.route("/index")
@auth_required
def index():
    return render_template("index.html", cuisines=mongo.db.cuisines.find().sort('cuisine_name', pymongo.ASCENDING))
    