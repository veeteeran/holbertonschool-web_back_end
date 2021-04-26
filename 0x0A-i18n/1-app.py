#!/usr/bin/env python3
"""Module of routes for task 0x0A"""
from datetime import datetime
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """Config class to setup Babel for English and French"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/')
def index():
    """Template for 1-index with title and header"""
    return render_template('1-index.html')


if __name__ == "__main__":
    host = "0.0.0.0"
    port = "5000"
