import os 
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId




    
app = Flask(__name__)

app.config["MONGO_DBNAME"] = "cooking_book"
app.config["MONGO_URI"] = 'mongodb+srv://root:onetwo@myfirstcluster-graej.mongodb.net/cooking_book?retryWrites=true'
mongo = PyMongo(app)



@app.route("/")
def index():
    return render_template("index.html", cuisines=mongo.db.cuisines.find())

@app.route('/get_recipe')
def get_recipe():
    return render_template("recipes.html", recipes=mongo.db.recipes.find())

@app.route("/mailto", methods=["GET","POST"])
def mailto():
    if request.method == "POST":
        flash("Thank you {}, we have recived your message!".format(request.form["name"]))
    return render_template("mailto.html", page_title="Send a message") 


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)