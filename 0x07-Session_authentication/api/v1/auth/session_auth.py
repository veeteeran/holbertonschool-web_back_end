#!/usr/bin/env python3
"""Session Auth Class module"""
from api.v1.auth.auth import Auth
from models.user import User
from os import getenv
from uuid import uuid4


class SessionAuth(Auth):
    """Session Auth inherits from Auth"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Creates a Session ID for a user_id"""
        if user_id is None or type(user_id) is not str:
            return None

        session_id = str(uuid4())
        self.user_id_by_session_id.update({session_id: user_id})

        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Returns a User ID based on a Session ID"""
        if session_id is None or type(session_id) is not str:
            return None

        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """Returns a User instance based on a cookie value
           Overloads method from Auth class
        """
        user_id = self.user_id_for_session_id(self.session_cookie(request))

        return User.get(user_id)

    def destroy_session(self, request=None):
        """Deletes the user session / logout"""
        if request is None:
            return False

        value = self.session_cookie(request)
        if value is None or self.user_id_for_session_id(value) is None:
            return False

        del self.user_id_by_session_id[value]

        return True
