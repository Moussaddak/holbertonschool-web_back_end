#!/usr/bin/env python3
""" Module of API Basic auth.
"""
import base64
import binascii
from typing import TypeVar

from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """
    BasicAuth class
    """

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """
            returns the Base64 part of the Authorization header
        Args:
            authorization_header:
        Returns:
        """
        if authorization_header is None \
                or not isinstance(authorization_header, str):
            return None
        container = authorization_header.split()
        if container[0] != "Basic":
            return None
        return container[-1]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """
            returns the decoded value of a Base64 string
        Args:
            base64_authorization_header:
        Returns:
        """
        if base64_authorization_header is None \
                or not isinstance(base64_authorization_header, str):
            return None
        container = base64_authorization_header.split()
        try:
            return base64.b64decode(container[-1],
                                    validate=True).decode('utf-8')
        except Exception as e:
            return None

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """
            returns the User instance based on his email and password.
        Args:
            user_email:
            user_pwd:
        Returns:
        """
        if not user_email or not user_pwd \
                or not isinstance(user_pwd, str) \
                or not isinstance(user_email, str):
            return None
        from models.user import User
        from models.base import DATA
        User.load_from_file()

        list_of_users = User.search({"email": user_email})
        if DATA is None or not len(list_of_users):
            return None
        user = list_of_users[0]
        if not user.is_valid_password(user_pwd):
            return None
        return user

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """
            returns the user email and password from the Base64 decoded value
        Args:
            decoded_base64_authorization_header:
        Returns:
        """
        if decoded_base64_authorization_header is None \
                or not isinstance(decoded_base64_authorization_header, str) \
                or ':' not in decoded_base64_authorization_header:
            return None, None
        user_email, user_password = decoded_base64_authorization_header\
            .split(':')
        return user_email, user_password

    def current_user(self, request=None) -> TypeVar('User'):
        """
            overloads Auth and retrieves the User instance for a request
        Args:
            request:
        Returns:
        """
        authorization = self.authorization_header(request)
        # print(authorization)
        auth_base64 = self.extract_base64_authorization_header(
            authorization)
        # print(auth_base64)
        auth_decoded = self.decode_base64_authorization_header(auth_base64)
        # print(auth_decoded)
        userCredential = self.extract_user_credentials(auth_decoded)
        # print(userCredential)
        userInstance = self.user_object_from_credentials(
            userCredential[0], userCredential[1])
        # print("userinstance {}".format(userInstance))
        return userInstance
