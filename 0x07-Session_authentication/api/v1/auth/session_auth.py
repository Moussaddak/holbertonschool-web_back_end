#!/usr/bin/env python3
""" Module of API Session Auth.
"""
import uuid

from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """
    SessionAuth class
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
            creates a Session ID for a user
        Args:
            user_id:

        Returns: session_id

        """
        if user_id is None or \
                not isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
            returns a User ID based on a Session ID
        Args:
            session_id:

        Returns:

        """
        if session_id is None \
                or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id, None)

    def current_user(self, request=None):
        """
            returns a User instance based on a cookie value
        Args:
            request:

        Returns:

        """
        from models.user import User
        session_id = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_id)
        return User.get(user_id)

    def destroy_session(self, request=None):
        """
            deletes the user session / logout
        Args:
            request:

        Returns:

        """
        if request is None \
                or self.session_cookie(request) is None:
            return False
        session_id = self.session_cookie(request)
        if self.user_id_for_session_id(session_id) is None:
            return False
        user_id = self.user_id_for_session_id(session_id)
        self.user_id_by_session_id.pop(user_id)
        return True
