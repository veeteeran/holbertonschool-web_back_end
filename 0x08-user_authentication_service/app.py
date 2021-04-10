#!/usr/bin/env python3
"""
Basic Flask app
"""
from auth import Auth
from flask import Flask, abort, jsonify, redirect, request, url_for


app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'])
def index():
    """ GET /
    Return:
    - jsonifiy {"message": "Bienvenue"}

    """
    return jsonify(message="Bienvenue")


@app.route('/users', methods=['POST'], strict_slashes=False)
def users():
    """ POST /users/
    Return:
        - Register user and return jsonified info or
        - 400 if user email in db
    """
    email = request.form['email']
    password = request.form['password']
    try:
        AUTH.register_user(email, password)
        return jsonify(email=email, message="user created")
    except ValueError:
        return jsonify(message="email already registered"), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    """ POST /sessions/
    Create new session, store session ID as cookie, key is session_id on the\
            response
    Return:
        - JSON payload of the form
        - 401 if login information is incorrect
    """
    email = request.form['email']
    password = request.form['password']

    if AUTH.valid_login(email, password):
        session_id = AUTH.create_session(email)
        response = jsonify(email=email, message="logged in")
        response.set_cookie('session_id', session_id)
        return response
    else:
        abort(401)


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout():
    """Logout and delete current session"""
    session_id = request.cookies.get('session_id')
    if session_id is None:
        return None

    user = AUTH.get_user_from_session_id(session_id)
    if user:
        AUTH.destroy_session(user.id)
        return redirect(url_for('index'))
    else:
        abort(403)


@app.route('/profile', methods=['GET'], strict_slashes=False)
def profile():
    """ GET /profile
    Find user if exists
    Return:
        - Status code 200
        - payload {"email": "<user email>"}
        - 403 if user does not exist or session_id invalid
    """
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    if user:
        return jsonify(email=user.email), 200
    else:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
