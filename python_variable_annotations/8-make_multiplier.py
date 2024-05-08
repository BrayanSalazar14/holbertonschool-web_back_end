#!/usr/bin/env python3
"""
type-annotated function make_multiplier that takes a float multiplier
as argument and returns a function that multiplies a float by multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a function that multiplies a given number by a specified multiplier.

    Args:
        multiplier (float): The multiplier to be used.

    Returns:
        Callable[[float], float]: A function that accepts a number and returns
        the result of multiplying it by the specified multiplier.
    """
    def mul(n: float) -> float:
        return n * multiplier
    return mul
