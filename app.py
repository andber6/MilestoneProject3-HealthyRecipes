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
    return render_template('recipes.html', 
                            recipes = recipe_list)

@app.route('/add_recipe')
def add_task():
    _categories = mongo.db.navigation.find()
    category_list = [category for category in _categories]
    return render_template('addrecipe.html',
                           categories=mongo.db.navigation.find())

@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.Creative_recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('get_recipes'))


if __name__ == "__main__":
    # app.run(host=os.environ.get('IP'),
    app.run(host="0.0.0.0",
        port=os.environ.get('PORT'),
        debug=True)