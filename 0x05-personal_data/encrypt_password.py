#!/usr/bin/env python3
"""Hash password module"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
        Returns a salted, hashed password as a byte string

            Parameter:
                    password(str): the password to hash
    """
    password = bytes(password, 'utf-8')
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())

    print(type(hashed))
    return hashed
