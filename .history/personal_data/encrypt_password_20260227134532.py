#!/usr/bin/env python3
"""
Module for password encryption using bcrypt.
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hashes a password using bcrypt with a salt.

    Args:
        password: The password string to hash

    Returns:
        A salted, hashed password as a byte string
    """
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Validates that a password matches a hashed password.

    Args:
        hashed_password: The hashed password as bytes
        password: The plain text password string to check

    Returns:
        True if the password matches the hash, False otherwise
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
