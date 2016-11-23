#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""passpass.py: Password Generator"""
__author__ = "Carlan Calazans"
__copyright__ = "Copyright 2016, Carlan Calazans"
__credits__ = ["Carlan Calazans"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Carlan Calazans"
__email__ = "carlancalazans at gmail dot com"
__status__ = "Development"

from flask import Flask, render_template, url_for, render_template
import random

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/', methods=['GET'])
def index():
    password = random.random()
    return render_template('index.html', password=password)

if __name__ == '__main__':
    app.run(host='0.0.0.0')