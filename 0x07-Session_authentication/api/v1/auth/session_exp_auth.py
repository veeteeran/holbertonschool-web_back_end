#!/usr/bin/env python3
"""SessionExpAuth Class module"""
from api.v1.auth.session_auth import SessionAuth
from datetime import datetime, timedelta
from os import getenv


class SessionExpAuth(SessionAuth):
    """SessionExpAuth inherits from SessionAuth"""
    def __init__(self):
        """Overloading the intit method"""
        if getenv('SESSION_DURATION'):
            self.session_duration = int(getenv('SESSION_DURATION'))
        else:
            self.session_duration = 0

    def create_session(self, user_id=None):
        """Creates a Session ID for a user_id"""
        session_id = super().create_session(user_id)
        if session_id is None:
            return None

        session_dict = {}
        self.user_id_by_session_id.update({session_id: session_dict})
        session_dict.update({'user_id': user_id,
                            'created_at': datetime.now()})

        return session_id

    def user_id_for_session_id(self, session_id=None):
        """Returns a User ID based on a Session ID"""
        if session_id is None:
            return None
        if self.user_id_by_session_id.get(session_id) is None:
            return None

        my_dict = self.user_id_by_session_id.get(session_id)
        if self.session_duration <= 0:
            return my_dict.get('user_id')

        created_at = my_dict.get('created_at')
        if created_at is None:
            return None

        session = created_at + timedelta(seconds=self.session_duration)
        if (session < datetime.now()):
            return None

        return my_dict.get('user_id')
