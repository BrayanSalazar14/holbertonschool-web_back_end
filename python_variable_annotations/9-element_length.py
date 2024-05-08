#!/usr/bin/env python3
"""
Annotate the below function’s parameters and
return values with the appropriate types
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calculate the length of each element in an iterable of sequences.

    Args:
        lst (Iterable[Sequence]): The input iterable containing sequences.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples,
        where each tuple contains a sequence and its length.
    """
    return [(i, len(i)) for i in lst]
