#!/usr/bin/env python3
"""
pagination modul
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, ...]:
    """
    return a tuple of size two containing a start index and an end index
    """
    tpl = tuple([(page - 1) * page_size, page * page_size])
    return tpl
