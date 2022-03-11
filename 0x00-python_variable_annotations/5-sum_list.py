#!/usr/bin/env python3
"""
moduel sum of list.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    returns return sum of list element.
    """
    x: int = 0
    for i in input_list:
        x += i
    return x
