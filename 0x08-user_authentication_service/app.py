#!/usr/bin/env python3
"""
Basic Flask app
"""
from auth import Auth
from flask import Flask, abort, jsonify, request


app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'])
def home():
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
    """ POST /seesions/
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
