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
    all_categories =  mongo.db.categories.find()
    _recipes = mongo.db.recipes.find()
    recipe_list = [recipe for recipe in _recipes]
    return render_template('recipes.html',
                            categories=all_categories,
                            recipes = recipe_list)

@app.route('/add_recipe')
def add_recipe():
    all_categories =  mongo.db.categories.find()
    return render_template('addrecipe.html',
                           categories=all_categories,
                           recipes=mongo.db.recipes.find())

@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return render_template('recipes.html',
                            categories=mongo.db.categories.find(),
                            recipes=mongo.db.recipes.find())

@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe =  mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    all_categories =  mongo.db.categories.find()
    return render_template('editrecipe.html', 
                           recipe=the_recipe,
                           categories=all_categories)

@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes
    all_categories =  mongo.db.categories.find()
    recipes.update({"_id": ObjectId(recipe_id)},
    {
        'category_name': request.form.get('category_name'),
        'recipe_name': request.form.get('recipe_name'),
        'recipe_description': request.form.get('recipe_description'),
        'ingredients': request.form.get('ingredients'),
        'isHealthy': request.form.get('isHealthy'),
        'isQuickToMake': request.form.get('isQuickToMake'),
        'submittedBy': request.form.get('submittedBy')
    })
    return render_template('recipes.html',
                            categories=all_categories,
                            recipes = mongo.db.recipes.find())

@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    all_categories =  mongo.db.categories.find()
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return render_template('recipes.html',
                            categories = all_categories,
                            recipes=mongo.db.recipes.find())

@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == "__main__":
    # app.run(host=os.environ.get('IP'),
    app.run(host="0.0.0.0",
        port=os.environ.get('PORT'),
        debug=False)