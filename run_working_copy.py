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

    
app = Flask(__name__)
Compress(app)


app.config["MONGO_DBNAME"] = "cooking_book"
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
DBS_NAME = 'cooking_book'
COLLECTION_NAME = 'recipes'
FIELDS = {'recipe_name': True, 'cuisine_name': True, 'preparation_time': True, 'cooking_time': True, 'date_posted':True, '_id': False}
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'flaskmail123@gmail.com'
app.config["MAIL_PASSWORD"] = 'marian87'

mail = Mail(app)
mongo = PyMongo(app)


    
@app.route("/")
def index():
    return render_template("index.html", cuisines=mongo.db.cuisines.find().sort('cuisine_name', pymongo.ASCENDING))

@app.route("/mailto",methods=['POST', 'GET'])
def mailto():
    return render_template("mailto.html", page_title="Send a message") 
    

@app.route('/send_mail', methods=['POST', 'GET'])
def send_mail():
    message = request.form['message']
    email = request.form['email']
    name = request.form['name']
    msg = Message(subject = """Message sent by  """ +str(name), sender=name , recipients=["flaskmail123@gmail.com"])
    msg.html = str(message) +"""<br>You can reply to """ +str(email)
    mail.send(msg)
    flash("We've recived your message")
    return redirect(url_for('mailto'))
    
@app.route("/login")
def login():
    return render_template('login.html')

    
@app.route('/login_form', methods=['POST'])
def login_form():
    users = mongo.db.users
    login_user = users.find_one({'name' : request.form['username']})
    
    if login_user:
        if bcrypt.hashpw(request.form['pass'].encode('utf-8'), login_user['password']) == login_user['password']:
            session['username'] = request.form['username']
            flash("You're logged in")
        return redirect(url_for('index'))
    return 'Invalid username or password'
    
    
@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name' : request.form['username']})
        
        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())
            users.insert({'name' : request.form['username'], 'password' : hashpass})
            session['username'] = request.form['username']
            flash("Your account has benn created")
            return redirect(url_for('index'))
        return 'That username already exists!'
    return render_template("register.html")


@app.route('/logout')
def logout():
    session.clear()
    flash("You've been logged successfully")
    return redirect(url_for('index'))


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
    # The code for the pagination was created with help from Shane Muirhead
    page_limit = 3
    current_page = int(request.args.get('current_page', 1))
    total = mongo.db.recipes.count()
    pages = range(1, int(math.ceil(total / page_limit)) + 1)
    recipes = mongo.db.recipes.find().sort('_id', pymongo.ASCENDING).skip((current_page - 1)*page_limit).limit(page_limit)
    
    return render_template('recipes.html', recipes=recipes, current_page=current_page, pages=pages)


@app.route('/search')
def search():
    #The code for the search functionlity was also created thanks to Shane Muirhead
    page_limit = 6 #Logic for pagination
    current_page = int(request.args.get('current_page', 1))
    db_query = request.args['db_query']
    total = mongo.db.recipes.find({'$text': {'$search': db_query }})
    t_total = len([x for x in total])
    pages = range(1, int(math.ceil(t_total / page_limit)) + 1)
    
    results = mongo.db.recipes.find({'$text': {'$search': db_query }}).sort('_id', pymongo.ASCENDING).skip((current_page - 1)*page_limit).limit(page_limit)
    return render_template('search.html', results=results, pages=pages, current_page=current_page)


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
        'date_posted': request.form.get('date_posted'),
        'image': request.form.get('image')
    })
    recipes.insert_one(new_recipe)
    flash("You've added a new recipe")
    return redirect(url_for('get_recipes'))


@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id":ObjectId(recipe_id)})
    all_cuisines = mongo.db.cuisines.find().sort('cuisine_name', pymongo.ASCENDING)
    return render_template('editrecipe.html', recipe=the_recipe, cuisines=all_cuisines)


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
        'method': request.form.getlist('step'),
        'date_posted': request.form.get('date_posted'),
        'image': request.form.get('image')
    })
    flash("You've updated the recipe successfully")
    return redirect(url_for('get_recipes'))
    
    
@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    flash("You've deleted the recipe successfully")
    return redirect(url_for('get_recipes'))
    
    
@app.route('/get_cuisines')
def get_cuisines():
    return render_template('cuisines.html', cuisines=mongo.db.cuisines.find().sort('cuisine_name', pymongo.ASCENDING))


@app.route('/recipes_for/<cuisine_id>')
def recipes_for(cuisine_id):
    the_cuisine = mongo.db.cuisines.find_one({"_id":ObjectId(cuisine_id)})
    all_recipes = mongo.db.recipes.find().sort('recipe_name', pymongo.ASCENDING)
    return render_template('recipesfor.html', recipes=all_recipes, cuisine=the_cuisine)
@app.route('/edit_cuisine/<cuisine_id>')
def edit_cuisine(cuisine_id):
    return render_template('editcuisine.html',
    cuisine=mongo.db.cuisines.find_one({'_id': ObjectId(cuisine_id)}))


@app.route('/update_cuisine/<cuisine_id>', methods=['POST'])
def update_cuisine(cuisine_id):
    mongo.db.cuisines.update(
        {'_id': ObjectId(cuisine_id)},
        {'cuisine_name': request.form.get('cuisine_name')})
    flash("You've updated the cuisine successfully")
    return redirect(url_for('get_cuisines'))


@app.route('/delete_cuisine/<cuisine_id>')
def delete_cuisine(cuisine_id):
    mongo.db.cuisines.remove({'_id': ObjectId(cuisine_id)})
    flash("You've deleted the cuisine successfully")
    return redirect(url_for('get_cuisines'))
    
@app.route('/new_cuisine')
def new_cuisine():
    return render_template('addcuisine.html')

@app.route('/insert_cuisine', methods=["POST"])
def insert_cuisine():
    cuisines = mongo.db.cuisines
    cuisine_data = {'cuisine_name': request.form.get('cuisine_name')}
    cuisines.insert_one(cuisine_data)
    flash("You've added a new cuisine")
    return redirect(url_for('get_cuisines'))

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True
        )