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
        from re import search
        if path is None or excluded_paths is None:
            return True
        if path and path[-1] != '/':
            path = path + '/'
        # if path in excluded_paths:
        #     return False
        for _path in excluded_paths:
            if '*' in _path and search(_path[:-1], path[:-1]):
                return False
            elif path in _path:
                return False
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

    def session_cookie(self, request=None):
        """
            returns a cookie value from a request
        Args:
            request:

        Returns:

        """
        if request is None:
            return None
        return request.cookies.get("_my_session_id")
