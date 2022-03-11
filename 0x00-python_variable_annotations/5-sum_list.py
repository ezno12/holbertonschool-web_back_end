#!/usr/bin/env python3
"""
moduel convert float to string.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    returns the string representation of the float.
    """
    x: int = 0
    for i in input_list:
        x += i
    return x
