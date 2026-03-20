#!/usr/bin/env python3
"""Authentication service utilities.

This module provides authentication helpers for user management.
It includes password hashing and user registration.
"""

import bcrypt
import uuid
from db import DB
from sqlalchemy.orm.exc import NoResultFound
from user import User


def _hash_password(password: str) -> bytes:
    """Hash a password with bcrypt and return the salted hash as bytes.

    Args:
        password (str): The plain text password to hash.

    Returns:
        bytes: The salted hash of the password.
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def _generate_uuid() -> str:
    """Generate a new UUID and return its string representation.

    Returns:
        str: The string representation of a new UUID.
    """
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.

    Provides methods for user registration and authentication.
    """

    def __init__(self) -> None:
        """Initialize the Auth class and set up the database handler."""
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register a new user with the given email and password.

        Args:
            email (str): The user's email address.
            password (str): The user's password.

        Returns:
            User: The created user object.

        Raises:
            ValueError: If a user with the given email already exists.
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError(
                "User {} already exists".format(email)
            )
        except NoResultFound:
            hashed = _hash_password(password)
            return self._db.add_user(email, hashed.decode('utf-8'))

    def valid_login(self, email: str, password: str) -> bool:
        """Validate user credentials.

        Args:
            email (str): The user's email address.
            password (str): The user's password.

        Returns:
            bool: True if credentials are valid, False otherwise.
        """
        try:
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(
                password.encode('utf-8'),
                user.hashed_password.encode('utf-8')
            )
        except Exception:
            return False

    def create_session(self, email: str) -> str:
        """Create a new session ID for the user and return it.

        Args:
            email (str): The user's email address.

        Returns:
            str: The session ID, or None if user not found.
        """
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        except Exception:
            return None

    def get_user_from_session_id(self, session_id: str) -> User:
        """Return the user linked to a session_id.

        Return None if no user matches the session ID or if it is None.

        Args:
            session_id (str): The session ID to search for.

        Returns:
            User: The user associated with the session_id, or None
            if not found.
        """
        if session_id is None:
            return None
        try:
            return self._db.find_user_by(session_id=session_id)
        except Exception:
            return None

    def destroy_session(self, user_id: int) -> None:
        """Destroy the session for a user by clearing session_id.

        Args:
            user_id (int): The ID of the user whose session
            should be destroyed.

        Returns:
            None
        """
        try:
            self._db.update_user(user_id, session_id=None)
        except Exception:
            pass

    def get_reset_password_token(self, email: str) -> str:
        """Generate and store a reset token for the user identified by email.

        Args:
            email (str): The email of the user requesting a password reset.

        Returns:
            str: The generated reset token.

        Raises:
            ValueError: If no user exists for the provided email.
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            raise ValueError()

        reset_token = _generate_uuid()
        self._db.update_user(user.id, reset_token=reset_token)
        return reset_token

    def update_password(self, reset_token: str, password: str) -> None:
        """Update a user's password using a valid reset token.

        Args:
            reset_token (str): Token used to identify the user resetting
            their password.
            password (str): The new plain text password.

        Raises:
            ValueError: If the reset token does not match any user.
        """
        try:
            user = self._db.find_user_by(reset_token=reset_token)
        except NoResultFound:
            raise ValueError()

        hashed_password = _hash_password(password).decode('utf-8')
        self._db.update_user(
            user.id,
            hashed_password=hashed_password,
            reset_token=None
        )
