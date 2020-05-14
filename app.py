import os
from flask_pymongo import PyMongo
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path

if os.path.exists("env.py"):
    import env

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'Recipe_Database'
app.config["MONGO_URI"]= os.environ.get('MONGO_URI')


mongo = PyMongo(app)

@app.route('/')
@app.route('/get_recipes')
def get_recipes():
    _recipes = mongo.db.Creative_recipes.find()
    recipe_list = [recipe for recipe in _recipes]
    return render_template("recipes.html", 
                            recipes = recipe_list)

@app.route('/add_recipe')
def add_task():
    _categories = mongo.db.navigation.find()
    category_list = [category for category in _categories]
    return render_template('addrecipe.html',
                           categories=mongo.db.navigation.find())

if __name__ == "__main__":
    app.run(host=os.environ.get('IP'),
        port=os.environ.get('PORT'),
        debug=True)