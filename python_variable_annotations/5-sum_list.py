#!/usr/bin/env python3
from typing import List

"""
type-annotated function sum_list which takes a list input_list
of floats as argument and returns their sum as a float.
"""


def sum_list(input_list: List[float]) -> float:
    """
    Calculate the sum of all elements in a list of floats.

    Args:
        input_list (List[float]): The input list of floating-point numbers.

    Returns:
        float: The sum of all elements in the input list.
    """
    return sum(input_list)
