#!/usr/bin/env python3
"""Basic Auth Class module"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """Basic Auth inherits from Auth"""
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
            Returns the Base64 part of the Authorization
            header for a Basic Authentication
        """
        if authorization_header is None:
            return None

        if type(authorization_header) is not str:
            return None

        if authorization_header[0:6] != 'Basic ':
            return None

        return authorization_header[6:]
