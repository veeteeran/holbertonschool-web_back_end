#!/usr/bin/env python3
""" Module of Auth class
"""
from flask import request
from models.user import User
from typing import List, TypeVar


class Auth():
    """Docstring for class Auth"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Require path method"""
        if path is None or excluded_paths is None or excluded_paths == []:
            return True

        if path[-1] != '/':
            path = path + '/'

        for ep in excluded_paths:
            if ep[-1] == '*':
                ep = ep[0:-1]

            if ep in path:
                return False

        if path not in excluded_paths:
            return True

        return False

    def authorization_header(self, request=None) -> str:
        """authorization_header method"""
        if request is None or request.headers.get('Authorization') is None:
            return None

        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """current_user method"""
        return None

    def session_cookie(self, request=None):
        """Returns a cookie value from a request"""
        if request is None:
            return None

        return request.cookies.get(getenv('SESSION_NAME'))
