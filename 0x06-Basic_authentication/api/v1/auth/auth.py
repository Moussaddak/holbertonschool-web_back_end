#!/usr/bin/env python3
""" Module of API authentication.
"""
from typing import List, TypeVar

from flask import request


class Auth:
    """
    Auth class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
            Define which routes don't need authentication
        Args:
            path:
            excluded_paths:

        Returns:

        """
        if path is None and excluded_paths is None:
            return True
        if path and path[-1] != '/':
            path = path + '/'
        if path in excluded_paths:
            return False
        elif path is None or path or not path:
            return True

    def authorization_header(self, request=None) -> str:
        """
            Request validation!
        Args:
            request:

        Returns:

        """
        if request is None or \
                request.headers.get("Authorization", None) is None:
            return None
        return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar('User'):
        """

        Args:
            request:

        Returns:

        """
        return None
