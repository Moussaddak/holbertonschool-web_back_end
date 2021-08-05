#!/usr/bin/env python3
"""
Encrypting passwords / Check valid password
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    Encrypting passwords
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Check valid password
    """
    return bcrypt.checkpw(password.encode(), hashed_password)
