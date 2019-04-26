import os 
import json
from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "key_one"

@app.route("/")
def index():
    data =[]
    with open("data/recipes.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("index.html", recipes=data) 


@app.route("/mailto", methods=["GET","POST"])
def mailto():
    if request.method == "POST":
        flash("Thank you {}, we have recived your message!".format(request.form["name"]))
    return render_template("mailto.html", page_title="Send a message") 


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)