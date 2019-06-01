import math
from flask import Flask, render_template, request, flash, redirect, url_for, Blueprint
from flask_pymongo import pymongo
from project import mongo
from bson.objectid import ObjectId


all_recipes = Blueprint('all_recipes', __name__)

@all_recipes.route('/get_recipes')
def get_recipes():
    # The code for the pagination was created with help from Shane Muirhead
    page_limit = 3
    current_page = int(request.args.get('current_page', 1))
    total = mongo.db.recipes.count()
    pages = range(1, int(math.ceil(total / page_limit)) + 1)
    recipes = mongo.db.recipes.find().sort('_id', pymongo.ASCENDING).skip((current_page - 1)*page_limit).limit(page_limit)
    
    return render_template('recipes.html', recipes=recipes, current_page=current_page, pages=pages)


@all_recipes.route('/search')
def search():
    #The code for the search functionlity was also created thanks to Shane Muirhead
    page_limit = 3 #Logic for pagination
    current_page = int(request.args.get('current_page', 1))
    db_query = request.args['db_query']
    total = mongo.db.recipes.find({'$text': {'$search': db_query }})
    t_total = len([x for x in total])
    pages = range(1, int(math.ceil(t_total / page_limit)) + 1)
    
    results = mongo.db.recipes.find({'$text': {'$search': db_query }}).sort('_id', pymongo.ASCENDING).skip((current_page - 1)*page_limit).limit(page_limit)
    return render_template('search.html', results=results, pages=pages, current_page=current_page)


@all_recipes.route('/add_recipe')
def add_recipe():
    return render_template('addrecipe.html', cuisines=mongo.db.cuisines.find().sort('cuisine_name', pymongo.ASCENDING))
    

@all_recipes.route('/insert_recipe',methods=["POST"])
def insert_recipe():
    recipes = mongo.db.recipes
    new_recipe = ({
        'recipe_name': request.form.get('recipe_name'),
        'cuisine_name': request.form.get('cuisine_name'),
        'preparation_time': request.form.get('preparation_time'),
        'cooking_time': request.form.get('cooking_time'),
        'serves': request.form.get('serves'),
        'ingredients': request.form.getlist('ingredient'),
        'method': request.form.getlist('step'),
        'date_posted': request.form.get('date_posted'),
        'image': request.form.get('image')
    })
    recipes.insert_one(new_recipe)
    flash("You've added a new recipe")
    return redirect(url_for('all_recipes.get_recipes'))


@all_recipes.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id":ObjectId(recipe_id)})
    all_cuisines = mongo.db.cuisines.find().sort('cuisine_name', pymongo.ASCENDING)
    return render_template('editrecipe.html', recipe=the_recipe, cuisines=all_cuisines)


@all_recipes.route('/update_recipe/<recipe_id>', methods=['POST'])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes
    recipes.update( {'_id': ObjectId(recipe_id)},
    {
        'recipe_name': request.form.get('recipe_name'),
        'cuisine_name': request.form.get('cuisine_name'),
        'preparation_time': request.form.get('preparation_time'),
        'cooking_time': request.form.get('cooking_time'),
        'serves': request.form.get('serves'),
        'ingredients': request.form.getlist('ingredient'),
        'method': request.form.getlist('step'),
        'date_posted': request.form.get('date_posted'),
        'image': request.form.get('image')
    })
    flash("You've updated the recipe successfully")
    return redirect(url_for('all_recipes.get_recipes'))
    
    
@all_recipes.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    flash("You've deleted the recipe successfully")
    return redirect(url_for('all_recipes.get_recipes'))
    