#!/usr/bin/env python3
"""Auth module"""
import bcrypt
from db import DB
from sqlalchemy.orm.exc import NoResultFound
from user import User


def _hash_password(password: str) -> str:
    """Return a salted hash of the input password"""
    hashed = bcrypt.hashpw(bytes(password, 'utf-8'), bcrypt.gensalt())

    return str(hashed)


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """Initialize an Auth object"""
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register a user and saves to db. Return ValueError if email in db"""
        try:
            user_exists = self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed_password = _hash_password(password)
            return self._db.add_user(email, hashed_password)
