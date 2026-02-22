from flask import Flask, render_template, request
import readcsv

app = Flask(__name__)

# GLOBAL VAR
available_recipes = []

@app.route("/")
def homepage():
    return render_template("index.html")

# Route to handle the form data
@app.route('/recipes', methods=['POST'])
def process_data():
    global available_recipes

    # update available_recipes
    user_ingredients = request.form.get('user_ingredients') or ""

    available_recipes = readcsv.getRecipes(user_ingredients)
    
    return render_template("recipes.html", recipes=available_recipes)

@app.route('/recipes')
def back_to_search_results():
    global available_recipes
    return render_template("recipes.html", recipes=available_recipes)

@app.route("/templates/specific/<recipeName>")
def specific_page(recipeName):

    ingredients= readcsv.getData(recipeName, "Ingredients")
    instructions = readcsv.getData(recipeName, "Preparation")
    return render_template("specific.html", title=recipeName, recipe_title=recipeName, ingredients=ingredients, instructions=instructions)

@app.route('/full')
def full_page():
    l = readcsv.fullList() #recipeList is the list of all the recipes
    return render_template("full.html", recipeList=l)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)