#!/usr/bin/env python3
"""
moduel tuple.
"""
from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    returns return tuple.
    """
    return (k, v**2)
