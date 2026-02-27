#!/usr/bin/env python3
""" BasicAuth module for API authentication
"""
from api.v1.auth.auth import Auth
from typing import TypeVar
from models.user import User
import base64


class BasicAuth(Auth):
    """ BasicAuth class that inherits from Auth
    """

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """ Extract the Base64 part of the Authorization header
        Args:
            authorization_header: the Authorization header string
        Returns:
            The Base64 part after 'Basic ' or None
        """
        if authorization_header is None:
            return None

        if not isinstance(authorization_header, str):
            return None

        if not authorization_header.startswith('Basic '):
            return None

        return authorization_header[6:]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """ Decode a Base64 authorization header
        Args:
            base64_authorization_header: the Base64 string to decode
        Returns:
            The decoded value as UTF-8 string or None
        """
        if base64_authorization_header is None:
            return None

        if not isinstance(base64_authorization_header, str):
            return None

        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            return decoded_bytes.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """ Extract user email and password from decoded Base64 string
        Args:
            decoded_base64_authorization_header: decoded Base64 string
        Returns:
            Tuple of (email, password) or (None, None)
        """
        if decoded_base64_authorization_header is None:
            return None, None

        if not isinstance(decoded_base64_authorization_header, str):
            return None, None

        if ':' not in decoded_base64_authorization_header:
            return None, None

        # Split on first ':' only to handle passwords with ':'
        credentials = decoded_base64_authorization_header.split(':', 1)
        return credentials[0], credentials[1]

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """ Get User instance based on email and password
        Args:
            user_email: user's email
            user_pwd: user's password
        Returns:
            User instance or None
        """
        if user_email is None or not isinstance(user_email, str):
            return None

        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        try:
            users = User.search({'email': user_email})
        except Exception:
            return None

        if not users or len(users) == 0:
            return None

        for user in users:
            if user.is_valid_password(user_pwd):
                return user

        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Retrieve the User instance for a request
        Args:
            request: Flask request object
        Returns:
            User instance or None
        """
        # Get the Authorization header from the request
        auth_header = self.authorization_header(request)
        if auth_header is None:
            return None

        # Extract the Base64 part
        base64_auth = self.extract_base64_authorization_header(auth_header)
        if base64_auth is None:
            return None

        # Decode the Base64 string
        decoded_auth = self.decode_base64_authorization_header(base64_auth)
        if decoded_auth is None:
            return None

        # Extract user credentials
        user_email, user_pwd = self.extract_user_credentials(decoded_auth)
        if user_email is None or user_pwd is None:
            return None

        # Get the User instance
        return self.user_object_from_credentials(user_email, user_pwd)
