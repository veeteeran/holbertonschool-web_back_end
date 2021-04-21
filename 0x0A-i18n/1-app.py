#!/usr/bin/env python3
"""Module of routes for task 0x0A"""
from flask import Flask, render_template, requests
from flask_babel import Babel

app = Flask(__name__)
app.config = Config()
babel = Babel(app)


@app.route('/')
def index():
    """Template for 0-index with title and header"""
    return render_template('0-index.html',
                           title='Welcome to Holberton',
                           header='Hello world')

class Config(object):
    """Config class to setup Babel for English and French"""
    LANGUAGES = ["en", "fr"]
    babel.default_locale = "en"
    babel.default_timezone = "UTC"

    '''
    @babel.localeselector
    def default_locale(self):
        """Config default locale to en"""
        return app.config['BABEL_DEFAULT_LOCALE'] = "en"

    @babel.timezoneselector
    def default_timezone(self):
        """Config default locale to UTC"""
        return app.config['BABEL_DEFAULT_TIMEZONE'] = "UTC"
    '''
