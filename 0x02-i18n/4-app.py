#!/usr/bin/env python3
"""
0-app
"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """Configure available languages."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Returns 4-index.html template
    """
    return render_template('4-index.html')


@babel.localeselector
def get_locale() -> str:
    """Determine the best match among our supported languages."""
    if request.args.get('locale'):
        locale = request.args.get('locale')
        if locale in app.config['LANGUAGES']:
            return locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
