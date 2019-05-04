import os 
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId




    
app = Flask(__name__)
app.secret_key = 'onetwo'

app.config["MONGO_DBNAME"] = "cooking_book"
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
mongo = PyMongo(app)



@app.route("/")
def index():
    return render_template("index.html", cuisines=mongo.db.cuisines.find())

@app.route('/get_recipe')
def get_recipe():
    return render_template("recipes.html", recipes=mongo.db.recipes.find())
    
@app.route('/add_recipe')
def add_recipe():
    return render_template('addrecipe.html', cuisines=mongo.db.cuisines.find())
    

@app.route('/insert_recipe',methods=["POST"])
def insert_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    print (request.form.getlist('ingredients'))
    return redirect(url_for('get_recipe'))
    
@app.route("/mailto", methods=["GET","POST"])
def mailto():
    if request.method == "POST":
        flash("Thank you {}, we have recived your message!".format(request.form["name"]))
    return render_template("mailto.html", page_title="Send a message") 


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)