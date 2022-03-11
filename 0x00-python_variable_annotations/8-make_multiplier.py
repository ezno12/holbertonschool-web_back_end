#!/usr/bin/env python3
"""
moduel multiple.
"""
from typing import List, Union, Tuple, Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    returns res of multiplication.
    """
    def func(x: float):
        """
        """
        return x * multiplier
    return func
