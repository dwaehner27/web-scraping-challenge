from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import mars_scrape

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

@app.route("/")
def index():
    mars_app = mongo.db.collection.find_one()
    return render_template("index.html", mars_data=mars_app)


@app.route("/scrape")
def scrape():
    data = mars_scrape.scrape()
    mongo.db.collection.update({}, data, upsert=True)
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)