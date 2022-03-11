#!/usr/bin/env python3
"""
moduel sum of list.
"""
from typing import List, Union


def to_kv(k: str, v: Union[int, float]) -> tuple:
    """
    returns return sum of list elements.
    """
    Li_st = [k, float((v**2))]
    tu_ple = tuple(Li_st)
    return tu_ple
