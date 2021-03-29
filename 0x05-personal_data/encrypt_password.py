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

    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
        Validate that the provided password matches the hashed password
        Return True if matches, Flase otherwise

            Parameters:
                    password(str): the password to hash
                    hashed_password(bytes): password after hash
    """
    if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
        return True
    else:
        return False
