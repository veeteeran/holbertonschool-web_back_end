#!/usr/bin/env python3
"""SessionDBAuth Class module"""
from api.v1.auth.session_exp_auth import SessionExpAuth
from models.base import DATA, Base
from models.user_session import UserSession


class SessionDBAuth(SessionExpAuth):
    """SessionDBAuth inherits from SessionExpAuth"""
    def create_session(self, user_id=None):
        """Creates a Session ID for a user_id"""
        session_id = super().create_session(user_id)
        new_session = UserSession()
        new_session.user_id = user_id
        new_session.session_id = session_id
        new_session.save()

        return session_id

    def user_id_for_session_id(self, session_id=None):
        """Returns a User ID based on a Session ID"""
        user_id = super().user_id_for_session_id(session_id)
        return user_id

    def destroy_session(self, request=None):
        """Deletes the user session / logout"""
        if request is None or self.session_cookie(request) is None:
            return False

        sessions = UserSession.all()
        for session in sessions:
            if session.session_id == self.session_cookie(request):
                del session

        return True
