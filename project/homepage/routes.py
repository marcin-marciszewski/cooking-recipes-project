from flask import Flask, render_template, request, flash, redirect, url_for, Blueprint
from flask_pymongo import pymongo
from project import mongo

homepage = Blueprint('homepage', __name__)

@homepage.route("/")
def index():
    return render_template("index.html", cuisines=mongo.db.cuisines.find().sort('cuisine_name', pymongo.ASCENDING))
    