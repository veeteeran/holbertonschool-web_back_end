#!/usr/bin/env python3
"""Module of routes for task 0x0A"""
from flask import Flask, g, render_template, request
from flask_babel import Babel, gettext

app = Flask(__name__)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """Config class to setup Babel for English and French"""
    LANGUAGES = ["en", "fr"]
    Babel.default_locale = "en"
    Babel.default_timezone = "UTC"


app.config.from_object(Config)


@app.route('/')
def index():
    """Template for 5-index with title and header"""
    logged_in_as = None
    if g.user:
        logged_in_as = gettext(u'logged_in_as', username=g.user.get('name'))

    return render_template('6-index.html',
                           home_title=gettext(u'home_title'),
                           home_header=gettext(u'home_header'),
                           logged_in_as=logged_in_as,
                           not_logged_in=gettext(u'not_logged_in'))


@babel.localeselector
def get_locale():
    """Get user locale"""
    locale = request.args.get('locale')
    if locale in Config.LANGUAGES:
        return locale

    if g.user:
        locale = g.user.get('locale')
        if locale in Config.LANGUAGES:
            return locale
        else:
            return 'fr'

    if request.headers.get('Accept-Language'):
        return request.headers.get('Accept-Language')[:2]

    return Babel.default_locale


def get_user(user_id):
    """get_user returns a user dictionary or None"""
    return users.get(user_id)


@app.before_request
def before_request():
    """find a user if any, and set it as a global"""
    user_id = request.args.get('login_as')
    if user_id:
        user_id = int(user_id)

    g.user = get_user(user_id)
    

if __name__ == "__main__":
    host = "0.0.0.0"
    port = "5000"
    app.run(host=host, port=port, debug=True)
