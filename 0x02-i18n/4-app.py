#!/usr/bin/env python3
"""
babel starts here
"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """
    config class for the languages
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale()->str:
    """
    Get the best-matching language for the user.
    """
    # Check if the 'locale' parameter is present in the request
    locale_param = request.args.get('locale')

    # If the 'locale' parameter is a supported language, use it
    if locale_param and locale_param in app.config['LANGUAGES']:
        return locale_param

    # Resort to the previous default behavior
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    task 1 function
    """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(debug=True)
