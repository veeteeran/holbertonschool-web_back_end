#!/usr/bin/env python3
"""Auth module"""
import bcrypt
from db import DB
from sqlalchemy.orm.exc import NoResultFound
from typing import Union
from user import User
from uuid import uuid4


def _hash_password(password: str) -> str:
    """Return a salted hash of the input password"""
    if type(password) is not str:
        return None

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
        if type(email) is not str or type(password) is not str:
            return None

        try:
            user_exists = self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed_password = _hash_password(password)
            return self._db.add_user(email, hashed_password)

    def valid_login(self, email: str, password: str) -> bool:
        """Locates user by email. Return True if password matches
        False if not"""
        if type(email) is not str or type(password) is not str:
            return None

        try:
            user = self._db.find_user_by(email=email)
            pwd = bytes(password, 'utf-8')
            hashed_pwd = bytes(user.hashed_password[2:-1], 'utf-8')
            if bcrypt.checkpw(pwd, hashed_pwd):
                return True
            else:
                return False
        except NoResultFound:
            return False

    def _generate_uuid(self) -> str:
        """Return a string representation of a new UUID"""
        return str(uuid4())

    def create_session(self, email: str) -> Union[str, None]:
        """Find the user corresponding to the email, generate a new UUID and\
                store it in the database as the user’s session_id
        Return session_id
        """
        if type(email) is not str:
            return None

        try:
            user = self._db.find_user_by(email=email)
            self._db.update_user(user.id, session_id=self._generate_uuid())
            return user.session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> Union[User, None]:
        """Returns a str or None"""
        if session_id is Nonei or type(session_id) is not str:
            return None

        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """Updates the corresponding user’s session ID to None"""
        if user_id is None or type(user_id) is not int:
            return None

        try:
            self._db.update_user(user_id, session_id=None)
        except NoResultFound:
            return None
