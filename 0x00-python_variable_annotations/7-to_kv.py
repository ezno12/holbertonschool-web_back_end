#!/usr/bin/env python3
"""
moduel sum of list.
"""
from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    returns return sum of list elements.
    """
    return (k, v**2)
