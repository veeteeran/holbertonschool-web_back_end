#!/usr/bin/env python3
"""Basic Auth Class module"""
from api.v1.auth.auth import Auth
from base64 import b64decode
from typing import Tuple


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

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                           str) -> str:
        """
            Returns the decoded value of a Base64 string
            base64_authorization_header
        """
        if base64_authorization_header is None:
            return None

        if type(base64_authorization_header) is not str:
            return None

        try:
            return b64decode(base64_authorization_header,
                             None, True).decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header:
                                 str) -> Tuple[str, str]:
        """
            Returns the user email and password from the Base64 decoded value
        """
        if decoded_base64_authorization_header is None:
            return (None, None)

        if type(decoded_base64_authorization_header) is not str:
            return (None, None)

        if ':' not in decoded_base64_authorization_header:
            return (None, None)

        auth_header = decoded_base64_authorization_header.split(':')

        return (auth_header[0], auth_header[1])
