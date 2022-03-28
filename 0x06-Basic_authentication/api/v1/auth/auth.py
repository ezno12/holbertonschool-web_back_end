#!/usr/bin/env python3
"""
API authentication.
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """
    authentication class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        authentication
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        authorization
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        current user
        """
        return None
