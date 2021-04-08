#!/usr/bin/env python3
"""Auth module"""
import bcrypt


def _hash_password(password: str) -> str:
    """Return a salted hash of the input password"""
    hashed = bcrypt.hashpw(bytes(password, 'utf-8'), bcrypt.gensalt())

    return str(hashed)
