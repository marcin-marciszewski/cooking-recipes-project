from flask import Flask, render_template, request, flash, redirect, url_for, Blueprint, make_response, session
from flask_pymongo import pymongo
from project import mongo
from bson.objectid import ObjectId
import math
from functools import wraps
from project import auth_required

all_cuisines = Blueprint('all_cuisines', __name__)

#List of all cuisines
@all_cuisines.route('/get_cuisines')
@auth_required
def get_cuisines():
    return render_template('cuisines.html', cuisines=mongo.db.cuisines.find().sort('cuisine_name', pymongo.ASCENDING))

#List of recipes for particular cuisine
@all_cuisines.route('/recipes_for/<cuisine_id>')
@auth_required
def recipes_for(cuisine_id):
    cuisine = mongo.db.cuisines.find_one({"_id":ObjectId(cuisine_id)})
    cuisines =  mongo.db.cuisines.find()
    recipes = mongo.db.recipes.find().sort('recipe_name', pymongo.ASCENDING)
    return render_template('recipesfor.html', recipes=recipes, cuisine=cuisine)
    
#Edit selected cuisine    
@all_cuisines.route('/edit_cuisine/<cuisine_id>')
@auth_required
def edit_cuisine(cuisine_id):
    return render_template('editcuisine.html',
    cuisine=mongo.db.cuisines.find_one({'_id': ObjectId(cuisine_id)}))

#Update selected cuisine
@all_cuisines.route('/update_cuisine/<cuisine_id>', methods=['POST'])
@auth_required
def update_cuisine(cuisine_id):
    mongo.db.cuisines.update(
        {'_id': ObjectId(cuisine_id)},
        {'cuisine_name': request.form.get('cuisine_name')})
    flash("You've updated the cuisine successfully")
    return redirect(url_for('all_cuisines.get_cuisines'))

#Delete selected cuisine
@all_cuisines.route('/delete_cuisine/<cuisine_id>')
@auth_required
def delete_cuisine(cuisine_id):
    mongo.db.cuisines.remove({'_id': ObjectId(cuisine_id)})
    flash("You've deleted the cuisine successfully")
    return redirect(url_for('all_cuisines.get_cuisines'))

#Add a new cuisine    
@all_cuisines.route('/new_cuisine')
@auth_required
def new_cuisine():
    return render_template('addcuisine.html')

#Insert a new cuisine to the data base
@all_cuisines.route('/insert_cuisine', methods=["POST"])
@auth_required
def insert_cuisine():
    cuisines = mongo.db.cuisines
    cuisine_data = {'cuisine_name': request.form.get('cuisine_name')}
    cuisines.insert_one(cuisine_data)
    flash("You've added a new cuisine")
    return redirect(url_for('all_cuisines.get_cuisines'))
