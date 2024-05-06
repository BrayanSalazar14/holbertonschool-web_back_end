#!/usr/bin/env python3
from typing import Sequence, Any, Optional

"""
Augment the following code with the correct duck-typed annotations
"""
# The types of the elements of the input are not known


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    if lst:
        return lst[0]
    else:
        return None
