#!/usr/bin/env python3
""" Auth class for API authentication
"""
from typing import List, TypeVar
from flask import request


class Auth:
    """ Auth class to manage API authentication
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Determine if authentication is required for a given path
        Args:
            path: the path to check
            excluded_paths: list of paths that don't require authentication
        Returns:
            True if authentication is required, False otherwise
        """
        if path is None:
            return True

        if excluded_paths is None or len(excluded_paths) == 0:
            return True

        # Normalize path to ensure it ends with /
        normalized_path = path if path.endswith('/') else path + '/'

        for excluded_path in excluded_paths:
            # Normalize excluded_path to ensure it ends with /
            normalized_excluded = (excluded_path if excluded_path.endswith('/')
                                   else excluded_path + '/')
            if normalized_path == normalized_excluded:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """ Get the authorization header from the request
        Args:
            request: Flask request object
        Returns:
            The value of the Authorization header or None
        """
        if request is None:
            return None

        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """ Get the current user from the request
        Args:
            request: Flask request object
        Returns:
            None - will be implemented later
        """
        return None
