#!/usr/bin/env python3
"""
0-app
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Dict, Union, Optional
from pytz import timezone, utc
import pytz.exceptions

app = Flask(__name__)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@app.before_request
def before_request():
    """
    find a user if any, and set it as a global on flask.g.user
    """
    login_as = request.args.get('login_as')
    user = get_user(login_as)
    if user:
        g.user = user


def get_user(login_as: [str, None]) -> Optional[Dict]:
    """
    returns a user dictionary or None if the ID cannot be found
    or if login_as was not passed."""
    if not login_as or int(login_as) not in users:
        return None
    return users[int(login_as)]


class Config:
    """Configure available languages."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Returns 6-index.html template
    """
    if hasattr(g, 'user'):
        username = g.user.get('name')
        return render_template('6-index.html', username=username)
    else:
        return render_template('6-index.html', username=None)


@babel.localeselector
def get_locale() -> str:
    """Determine the best match among our supported languages."""
    if request.args.get('locale'):
        locale = request.args.get('locale')
        if locale in app.config['LANGUAGES']:
            return locale
    elif g.user:
        locale = g.user.get('locale')
        if locale in app.config['LANGUAGES']:
            return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """The function infers appropritate timezone"""
    if request.args.get('timezone'):
        timezone_query = request.args.get('timezone')
        try:
            return timezone(timezone_query).zone
        except pytz.exceptions.UnknownTimeZoneError:
            return None
    elif g.user:
        timezone_query = g.user.get('timezone')
        try:
            return timezone(timezone_query).zone
        except pytz.exceptions.UnknownTimeZoneError:
            return None
    return utc.zone


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
