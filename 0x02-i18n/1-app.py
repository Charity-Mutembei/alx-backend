#!/usr/bin/env python3
"""
babel starts here
"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """
    config class  for the languages
    """
    LANGUAGES = ["en", "fr"]


babel.init_app(app)
app.config.from_object(Config)
babel.default_locale = 'en'
babel.default_timezone = 'UTC'


@app.route('/')
def index():
    """
    task 1 function
    """
    return render_template('0-index.html')
