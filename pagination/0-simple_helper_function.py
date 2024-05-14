#!/usr/bin/env python3
"""
Module index_range that takes two integer arguments page and page_size
"""


def index_range(page, page_size):
    """
    Calculate the start and end indices for a given page and page size.

    Parameters:
        page (int): The page number.
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple containing the start index (inclusive) and
        end index (exclusive) for the specified page.
        The start index is calculated as (page - 1) * page_size,
        and the end index as page * page_size.
    """
    start_index, end_index = (page - 1) * page_size, page * page_size
    return (start_index, end_index)
