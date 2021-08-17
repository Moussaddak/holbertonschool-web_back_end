#!/usr/bin/env python3
"""
Module of Auth
"""
import uuid

import bcrypt
from sqlalchemy.orm.exc import NoResultFound

from db import DB
from user import User


def _hash_password(password: str) -> bytes:
    """
        Hash password
    :param password:
    :return:
    """
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed


def _generate_uuid() -> str:
    """
        Generate UUIDs
    :return:
    """
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
            register_user
        :param email:
        :param password:
        :return:
        """
        try:
            user = self._db.find_user_by(email=email)
            if user:
                raise ValueError("User {} already exists".format(email))
        except NoResultFound:
            hashed = _hash_password(password)
            return self._db.add_user(email, hashed)

    def valid_login(self, email: str, password: str) -> bool:
        """

        :param email:
        :param password:
        :return:
        """
        if email is None or password is None:
            return None
        try:
            user = self._db.find_user_by(email=email)
            _password = password.encode('utf-8')
            return bcrypt.checkpw(_password, user.hashed_password)
        except Exception as e:
            return False

    def create_session(self, email: str) -> str:
        """
            Get session ID
        :param email:
        :return:
        """

        if email is None:
            return None
        try:
            user = self._db.find_user_by(email=email)
            UUID = _generate_uuid()
            self._db.update_user(user.id, session_id=UUID)
            return UUID
        except Exception as e:
            return None

    def get_user_from_session_id(self, session_id: str) -> User:
        """
             Find user by session ID
        :param session_id:
        :return:
        """
        if not session_id:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except Exception as e:
            return None

    def destroy_session(self, user_id: int) -> None:
        """
            Destroy session
        :param user_id:
        :return:
        """
        if not user_id:
            return None
        try:
            user = self._db.update_user(user_id, session_id=None)
            return None
        except Exception as e:
            return None
