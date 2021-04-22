#!/usr/bin/env python3
"""Module of routes for task 0x0A"""
from flask import Flask, g, render_template, request
from flask_babel import Babel
from pytz import timezone, UnknownTimeZoneError

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
    """Template for 6-index with title and header"""
    return render_template('6-index.html')


@babel.localeselector
def get_locale():
    """Get user locale"""
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale

    if g.user:
        locale = g.user.get('locale')
        if locale and locale in app.config['LANGUAGES']:
            return locale

    accepted = request.headers.get('Accept-Language')
    if accepted and accepted in app.config['LANGUAGES']:
        return accepted

    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user():
    """get_user returns a user dictionary or None"""
    user_id = request.args.get('login_as')
    if user_id:
        return users.get(int(user_id))

    return None


@app.before_request
def before_request():
    """find a user if any, and set it as a global"""
    g.user = get_user()


@babel.timezoneselector
def get_timezone():
    """get_timezone returns user timezone"""
    timezone = request.get('timezone')
    if timezone:
        try:
            return timezone(timezone)
        except UnknownTimeZoneError:
            pass

    if g.user:
        timezone = request.get('timezone')
        if timezone:
            try:
                return timezone(timezone)
            except UnknownTimeZoneError:
                pass

    return Babel.default_timezone


if __name__ == "__main__":
    host = "0.0.0.0"
    port = "5000"
    app.run(host=host, port=port, debug=True)
