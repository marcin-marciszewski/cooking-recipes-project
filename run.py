import os 
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId
from pymongo import MongoClient
import json
from bson import json_util
from bson.json_util import dumps

    
app = Flask(__name__)
app.secret_key = 'onetwo'

app.config["MONGO_DBNAME"] = "cooking_book"
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
DBS_NAME = 'cooking_book'
COLLECTION_NAME = 'recipes'
FIELDS = {'recipe_name': True, 'cuisine_name': True, 'preparation_time': True, 'cooking_time': True, 'date_posted':True, '_id': False}

mongo = PyMongo(app)



@app.route("/")
def index():
    return render_template("index.html", cuisines=mongo.db.cuisines.find().sort('cuisine_name', pymongo.ASCENDING))


@app.route("/statistics")
def statistics():
    return render_template("statistics.html")


@app.route("/statistics/recipes")
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

@app.route('/get_recipes')
def get_recipes():
    return render_template("recipes.html", recipes=mongo.db.recipes.find().sort('recipe_name', pymongo.ASCENDING))



@app.route('/add_recipe')
def add_recipe():
    return render_template('addrecipe.html', cuisines=mongo.db.cuisines.find().sort('cuisine_name', pymongo.ASCENDING))
    

@app.route('/insert_recipe',methods=["POST"])
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
        'date_posted': request.form.get('date_posted')
    })
    recipes.insert_one(new_recipe)
    return redirect(url_for('get_recipes'))


@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id":ObjectId(recipe_id)})
    all_cuisines = mongo.db.cuisines.find().sort('cuisine_name', pymongo.ASCENDING)
    
    
    return render_template('editrecipe.html', recipe=the_recipe, cuisines=all_cuisines)
    
@app.route('/recipes_for/<cuisine_id>')
def recipes_for(cuisine_id):
    the_cuisine = mongo.db.cuisines.find_one({"_id":ObjectId(cuisine_id)})
    all_recipes = mongo.db.recipes.find().sort('recipe_name', pymongo.ASCENDING)
    
    return render_template('recipesfor.html', recipes=all_recipes, cuisine=the_cuisine)


    
    
@app.route('/update_recipe/<recipe_id>', methods=['POST'])
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
        'method': request.form.getlist('step')
    })
    return redirect(url_for('get_recipes'))
    
    
@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('get_recipes'))
    
    
@app.route('/get_cuisines')
def get_cuisines():
    return render_template('cuisines.html',
    cuisines=mongo.db.cuisines.find().sort('cuisine_name', pymongo.ASCENDING))
    

@app.route('/edit_cuisine/<cuisine_id>')
def edit_cuisine(cuisine_id):
    return render_template('editcuisine.html',
    cuisine=mongo.db.cuisines.find_one({'_id': ObjectId(cuisine_id)}))
    

    

@app.route('/update_cuisine/<cuisine_id>', methods=['POST'])
def update_cuisine(cuisine_id):
    mongo.db.cuisines.update(
        {'_id': ObjectId(cuisine_id)},
        {'cuisine_name': request.form.get('cuisine_name')})
    return redirect(url_for('get_cuisines'))



@app.route('/delete_cuisine/<cuisine_id>')
def delete_cuisine(cuisine_id):
    mongo.db.cuisines.remove({'_id': ObjectId(cuisine_id)})
    return redirect(url_for('get_cuisines'))


@app.route('/insert_cuisine', methods=["POST"])
def insert_cuisine():
    cuisines = mongo.db.cuisines
    cuisine_data = {'cuisine_name': request.form.get('cuisine_name')}
    cuisines.insert_one(cuisine_data)
    return redirect(url_for('get_cuisines'))
    

@app.route('/new_cuisine')
def new_cuisine():
    return render_template('addcuisine.html')
    
    
@app.route("/mailto", methods=["GET","POST"])
def mailto():
    if request.method == "POST":
        flash("Thank you {}, we have recived your message!".format(request.form["name"]))
    return render_template("mailto.html", page_title="Send a message") 
    
    
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True
        )