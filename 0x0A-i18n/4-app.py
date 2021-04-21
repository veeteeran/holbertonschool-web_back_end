#!/usr/bin/env python3
"""Module of routes for task 0x0A"""
from flask import Flask, g, render_template, request
from flask_babel import Babel, gettext

app = Flask(__name__)
babel = Babel(app)



class Config(object):
    """Config class to setup Babel for English and French"""
    LANGUAGES = ["en", "fr"]
    Babel.default_locale = "en"
    Babel.default_timezone = "UTC"


app.config.from_object(Config)


@app.route('/')
def index():
    """Template for 4-index with title and header"""
    return render_template('4-index.html',
                           home_title=gettext(u'home_title'),
                           home_header=gettext(u'home_header'))


@babel.localeselector
def get_locale():
    """Get user locale"""
    locale = request.args.get('locale')
    if locale in Config.LANGUAGES:
        return locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    host = "0.0.0.0"
    port = "5000"
    app.run(host=host, port=port, debug=True)
