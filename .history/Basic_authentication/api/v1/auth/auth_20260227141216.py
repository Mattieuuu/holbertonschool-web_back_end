#!/usr/bin/env python3
"""
Auth class module for managing API authentication
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """
    Auth class to manage API authentication
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if authentication is required for a given path

        Args:
            path: The path to check
            excluded_paths: List of paths that don't require authentication

        Returns:
            True if authentication is required, False otherwise
        """
        if path is None:
            return True

        if excluded_paths is None or len(excluded_paths) == 0:
            return True

        # Normalize path by ensuring it ends with /
        normalized_path = path if path.endswith('/') else path + '/'

        # Check if the normalized path is in excluded_paths
        for excluded_path in excluded_paths:
            if normalized_path == excluded_path:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        Gets the authorization header from the request

        Args:
            request: Flask request object

        Returns:
            None for now (will be implemented later)
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Gets the current user from the request

        Args:
            request: Flask request object

        Returns:
            None for now (will be implemented later)
        """
        return None
