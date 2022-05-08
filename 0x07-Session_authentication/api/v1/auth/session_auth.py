#!/usr/bin/env python3
"""
session authentication moduel
"""
from ast import Not
from api.v1.auth.auth import Auth
from uuid import uuid4


class SessionAuth(Auth):
    """
    session authentication class
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        method to create session for user
        """
        if user_id is None or type(user_id) is not str:
            return None
        else:
            sessionID = str(uuid4())
            self.user_id_by_session_id = {sessionID: user_id}
            return sessionID
