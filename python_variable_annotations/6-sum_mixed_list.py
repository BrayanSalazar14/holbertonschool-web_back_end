#!/usr/bin/env python3
from typing import Union, List

"""
type-annotated function sum_mixed_list which takes a list mxd_lst
of integers and floats and returns their sum as a float.
"""


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculate the sum of all elements in a list containing a mixture
    of integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): The input list containing
        a mixture of integers and floats.

    Returns:
        float: The sum of all elements in the input list.
    """
    return sum(mxd_lst)
