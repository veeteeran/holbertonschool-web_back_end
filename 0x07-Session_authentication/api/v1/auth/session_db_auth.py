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
        '''
        print(f"DATA: {DATA}")
        print(f"user_id_by_session_id: {self.user_id_by_session_id}")
        print(f"session_id: {session_id}")
        '''
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """Returns a User ID based on a Session ID"""
        #session_dict = self.user_id_by_session_id.get(session_id)
        #return session_dict.get('user_id')
        user_id = super().user_id_for_session_id(session_id)
        return user_id

    def destroy_session(self, request=None):
        """Deletes the user session / logout"""
        super().destroy_session(request)
