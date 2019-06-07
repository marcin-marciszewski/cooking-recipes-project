from flask import Flask, render_template, request, flash,session, redirect, url_for, Blueprint
from flask_pymongo import pymongo
from project import mongo

homepage = Blueprint('homepage', __name__)

@homepage.route("/")
def welcome():
    return render_template("welcome.html")

@homepage.route("/index")
def index():
    if session:
        return render_template("index.html", cuisines=mongo.db.cuisines.find().sort('cuisine_name', pymongo.ASCENDING))
    return 'Please login first'