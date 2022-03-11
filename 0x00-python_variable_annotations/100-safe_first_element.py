#!/usr/bin/env python3
"""Annotated Function"""
from typing import Any, Union


def safe_first_element(lst: Any) -> Union[Any, None]:
    if lst:
        return lst[0]
    else:
        return None
