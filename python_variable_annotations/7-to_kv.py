#!/usr/bin/env python3
from typing import Union, Tuple
"""
type-annotated function to_kv that takes a string k and an int OR float v
as arguments and returns a tuple.
The first element of the tuple is the string k
The second element is the square of the int/float v
and should be annotated as a float.
"""


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple containing the square of a number associated with a key.

    Args:
        k (str): The key.
        v (Union[int, float]): The value
        (an integer or a floating-point number).

    Returns:
        Tuple[str, float]: A tuple containing the
        key and the square of the value.
    """
    return (k, v ** 2)
