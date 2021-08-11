#!/usr/bin/env python3
"""
Module of API Session ExpAuth
"""
from api.v1.auth.session_auth import SessionAuth
from datetime import datetime, timedelta
import os


class SessionExpAuth(SessionAuth):
    """
    SessionExpAuth Class
    """

    def __init__(self):
        """ initialization
        """
        self.session_duration = int(os.getenv("SESSION_DURATION")) \
            if os.getenv("SESSION_DURATION") else 0

    def create_session(self, user_id=None):
        """
            Create a Session ID
        Args:
            user_id:

        Returns:

        """
        session_id = super(SessionExpAuth, self).create_session(user_id)
        if session_id is None:
            return None

        self.user_id_by_session_id[session_id] = {
            "user_id": user_id, "created_at": datetime.now()}
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """
            Overload user_id_for_session_id
        Args:
            session_id:

        Returns:

        """

        if session_id is None or \
                session_id not in self.user_id_by_session_id.keys():
            return None
        if self.session_duration <= 0:
            return self.user_id_by_session_id[session_id]["user_id"]
        if "created_at" not in self.user_id_by_session_id[session_id]:
            return None
        createdAt = self.user_id_by_session_id[session_id]["created_at"]
        TotalRunningTime = createdAt + timedelta(seconds=self.session_duration)
        if TotalRunningTime < datetime.now():
            return None

        return self.user_id_by_session_id[session_id]['user_id']
