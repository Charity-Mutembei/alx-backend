#!/usr/bin/env python3
"""
babel starts here
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, _

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

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(user_id):
    """
    Get user dictionary by ID or return None if not found.
    """
    return users.get(user_id)


@app.before_request
def before_request():
    """
    Execute before all other functions, set user on flask.g.
    """
    user_id = request.args.get('login_as', type=int)
    g.user = get_user(user_id)


@babel.localeselector
def get_locale():
    """
    Get the best-matching language for the user.
    """

    url_locale = request.args.get('locale')
    if url_locale and url_locale in app.config['LANGUAGES']:
        return url_locale

    if g.user and g.user['locale'] in app.config["LANGUAGES"]:
        return g.user['locale']

    header_locale = request.headers.get('Accept-Language')
    if header_locale:
        header_locale = header_locale.split(',')[0].strip().lower()
        if header_locale in app.config['LANGUAGES']:
            return header_locale

    return app.config['BABEL_DEFAULT_LOCALE']


@app.route('/')
def index():
    """
    task 1 function
    """
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(debug=True)
