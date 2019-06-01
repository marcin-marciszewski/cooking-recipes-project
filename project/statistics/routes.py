import os
from flask import Flask, render_template, request, flash, redirect, url_for, Blueprint
from pymongo import MongoClient
from bson.json_util import dumps
import json
from bson import json_util
DBS_NAME = 'cooking_book'
COLLECTION_NAME = 'recipes'
FIELDS = {'recipe_name': True, 'cuisine_name': True, 'preparation_time': True, 'cooking_time': True, 'date_posted':True, '_id': False}
statistics_function = Blueprint('statistics_function', __name__)



@statistics_function.route("/statistics")
def statistics():
    return render_template("statistics.html")


@statistics_function.route("/statistics/recipes")
def recipes():
    connection = MongoClient(os.environ.get("MONGO_URI"))
    collection = connection[DBS_NAME][COLLECTION_NAME]
    recipes = collection.find(projection=FIELDS)
    json_recipes = []
    for recipe in recipes:
        json_recipes.append(recipe)
    json_recipes = json.dumps(json_recipes, default=json_util.default)
    connection.close()
    return json_recipes