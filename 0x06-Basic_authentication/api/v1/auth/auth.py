#!/usr/bin/env python3
""" Module of Auth class
"""
from flask import request
from models.user import User
from typing import List, TypeVar


class Auth():

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Require path method"""
        return False

    def authorization_header(self, request=None) -> str:
        """authorization_header method"""
        return request

    def current_user(self, request=None) -> TypeVar('User'):
        """current_user method"""
        return request
