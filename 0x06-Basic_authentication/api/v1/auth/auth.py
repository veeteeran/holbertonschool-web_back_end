#!/usr/bin/env python3
""" Module of Auth class
"""
from flask import request
from models.user import User
import re
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
            regex = f"{ep}.*"
            match = re.search(regex, path)
            if not match:
                return True

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
