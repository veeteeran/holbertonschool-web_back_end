#!/usr/bin/env python3
"""Integration test module for Flask app"""
import requests


def register_user(email: str, password: str) -> None:
    """Test register user route"""
    payload = {'email': email, 'password': password}
    r = requests.post('http://127.0.0.1:5000/users', data=payload)
    assert r.raise_for_status() is None, f"Status code is {r.status_code}"
    assert r.json() == {'email': email, "message": "user created"}


def log_in_wrong_password(email: str, password: str) -> None:
    """Test login with wrong password"""
    payload = {'email': email, 'password': password}
    r = requests.post('http://127.0.0.1:5000/sessions', data=payload)
    assert r.status_code == 401, f"Status code is {r.status_code}"


def log_in(email: str, password: str) -> str:
    """Test login with correct password"""
    payload = {'email': email, 'password': password}
    r = requests.post('http://127.0.0.1:5000/sessions', data=payload)
    assert r.raise_for_status() is None, f"Status code is {r.status_code}"
    assert r.json() == {'email': email, "message": "logged in"}


def profile_unlogged() -> None:
    """Test /profile route with invalid input"""
    no_cookie = None
    fake_cookie = dict(session_id='not-a-real-cookie')
    r = requests.get('http://127.0.0.1:5000/profile', cookies=no_cookie)
    f = requests.get('http://127.0.0.1:5000/profile', cookies=fake_cookie)
    assert r.status_code == 403, f"Status code is {r.status_code}"
    assert f.status_code == 403, f"Status code is {r.status_code}"


def profile_logged(session_id: str) -> None:
    """Test /profile route with valid input"""
    pass


def log_out(session_id: str) -> None:
    """Test /sessions route DELETE method"""
    pass


def reset_password_token(email: str) -> str:
    """Test /reset_password POST method, creates a password"""
    pass


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """Test /reset_password PUT method, update a password"""
    pass


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


if __name__ == "__main__":

    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    '''
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
    '''
