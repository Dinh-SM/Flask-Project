#!/usr/bin/env python3
# coding: utf-8

from flask import Flask, g, json
from flask import abort, request, make_response
from flask import render_template
from database import get_recipe, get_recipes, get_ingredients

import re


app = Flask(__name__)


@app.route('/')
def index():
    app.logger.debug('serving root URL /')
    return render_template('index.html')


@app.route('/recettes')
def recettes():
    recipes = get_recipes()
    card_deck_nb = int(len(recipes) / 3)
    to_hide = len(recipes) % 3
    app.logger.debug("card " + str(card_deck_nb) + " hide " + str(to_hide))
    return render_template('recettes.html', recipes = recipes, card_deck_nb = card_deck_nb, to_show = len(recipes), to_hide = to_hide)

@app.route('/recette')
def recette():
    app.logger.debug('serving root URL /')
    return render_template('recette.html')

@app.route('/advanced-search')
def advanced_search():
    app.logger.debug('serving root URL /')
    return render_template('advanced-search.html')


@app.route('/contact')
def contact():
    app.logger.debug('serving root URL /')
    return render_template('contact.html')


# Script starts here
if __name__ == '__main__':
    from os import environ
    DEBUG = environ.get('DEBUG')
    app.run(port=8000, debug=DEBUG)