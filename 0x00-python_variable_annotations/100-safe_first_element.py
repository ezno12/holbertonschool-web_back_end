#!/usr/bin/env python3
"""Annotated Function"""
from typing import Any, Union, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    anno func
    """
    if lst:
        return lst[0]
    else:
        return None
