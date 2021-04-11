#!/usr/bin/env python3
# coding: utf-8

from flask import Flask, g, json
from flask import abort, request, make_response
from flask import render_template
from database import get_recipe, get_recipes, add_comment, reset_database

import re
from datetime import date


app = Flask(__name__)


@app.route('/')
def index():
    app.logger.debug('serving root URL /')
    return render_template('index.html')


@app.route('/recettes', methods=["GET"])
def recettes():
    if request.args.get("q"):
        app.logger.debug(request.args.get("q"))
        recipes = get_recipes()
        filtered_recipes = []
        for recipe in recipes:
            if re.search("^.*" + request.args.get("q") + ".*$", recipe["name"], re.IGNORECASE) and (recipe not in filtered_recipes):
                filtered_recipes.append(recipe)
            for ingredient in recipe["ingredients"]:
                if re.search("^.*" + request.args.get("q") + ".*$", ingredient, re.IGNORECASE) and (recipe not in filtered_recipes):
                    filtered_recipes.append(recipe)
        app.logger.debug(len(filtered_recipes))
        
        card_deck_nb = int(len(filtered_recipes) / 3)
        to_hide = 3-len(filtered_recipes) % 3
        if to_hide > 0:
            card_deck_nb += 1
        return render_template('recettes.html', recipes = filtered_recipes, card_deck_nb = card_deck_nb, to_hide = to_hide)

    else:
        recipes = get_recipes()
        card_deck_nb = int(len(recipes) / 3)
        to_hide = 3-len(recipes) % 3
        if to_hide > 0:
            card_deck_nb += 1
        return render_template('recettes.html', recipes = recipes, card_deck_nb = card_deck_nb, to_hide = to_hide)

@app.route('/recette')
@app.route('/recette/<recipe_id>', methods=['GET', 'POST'])
def recette(recipe_id = None):
    if recipe_id and request.method != 'POST':
        app.logger.debug('Recipe ID' + str(recipe_id))
        recipe = get_recipe(recipe_id)
        if not recipe:
            app.logger.debug('404 NOT FOUND')
            abort(404)
        app.logger.debug(recipe['name'])
        return render_template('recette.html', recipe = recipe)
    elif recipe_id and request.method == 'POST':
        app.logger.debug(request.form)
        new_comment = {
            "author": request.form['author'],
            "date": date.today().strftime("%d-%m-%Y"),
            "content": request.form['content']
        }
        app.logger.debug(new_comment)
        add_comment(recipe_id, new_comment)
        recipe = get_recipe(recipe_id)
        if not recipe:
            app.logger.debug('404 NOT FOUND')
            abort(404)
        app.logger.debug(recipe['comments'])
        return render_template('recette.html', recipe = recipe)
    app.logger.debug('404 NOT FOUND')
    abort(404)


@app.route('/contact')
def contact():
    app.logger.debug('serving root URL /contact')
    return render_template('contact.html')


@app.route('/reset')
def reset():
    app.logger.debug('serving root URL /reset')
    reset_database()
    return render_template('index.html')


# Script starts here
if __name__ == '__main__':
    from os import environ
    DEBUG = environ.get('DEBUG')
    app.run(port=8000, debug=DEBUG)