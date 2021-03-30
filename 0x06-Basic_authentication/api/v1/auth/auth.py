#!/usr/bin/env python3
""" Module of Auth class
"""
from flask import request
from models.user import User
from typing import List, TypeVar


class Auth():

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Require path method"""
        if path is not None and path[-1] != '/':
            path = path + '/'

        if path is None or excluded_paths is [] or path not in excluded_paths:
            return True

        return False

    def authorization_header(self, request=None) -> str:
        """authorization_header method"""
        return request

    def current_user(self, request=None) -> TypeVar('User'):
        """current_user method"""
        return request
