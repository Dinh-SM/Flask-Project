#!/usr/bin/env python3
# coding: utf-8

from flask import Flask, g, json
from flask import abort, request, make_response
from flask import render_template

import re


app = Flask(__name__)


@app.route('/')
def index():
    app.logger.debug('serving root URL /')
    return render_template('index.html')


@app.route('/recettes')
def recettes():
    app.logger.debug('serving root URL /')
    return render_template('recettes.html')

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