#!/usr/bin/env python3
"""Module of routes for task 0x0A"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)
Babel.default_locale = "en"
Babel.default_timezone = "UTC"


@app.route('/')
def index():
    """Template for 2-index with title and header"""
    return render_template('2-index.html',
                           title='Welcome to Holberton',
                           header='Hello world')

class Config(object):
    """Config class to setup Babel for English and French"""
    LANGUAGES = ["en", "fr"]

    @babel.localeselector
    def get_locale(self):
        """Get user locale"""
        return request.accept_languages.best_match(app.config['LANGUAGES'])

    '''
    @babel.timezoneselector
    def default_timezone(self):
        """Config default locale to UTC"""
        return app.config['BABEL_DEFAULT_TIMEZONE'] = "UTC"
    '''


if __name__ == "__main__":
    host = "0.0.0.0"
    port = "5000"
    app.run(host=host, port=port, debug=True)
