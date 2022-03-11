#!/usr/bin/env python3
"""
moduel sum of list.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    returns return sum of list elements.
    """
    x: int = 0
    for i in mxd_lst:
        x += i
    return x
