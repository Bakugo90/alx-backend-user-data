#!/usr/bin/env python3
"""Password encryption.
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """Hashing password
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Checking if a hashed password .
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
