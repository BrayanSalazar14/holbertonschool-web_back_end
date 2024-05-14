#!/usr/bin/env python3
"""
Module index_range that takes two integer arguments page and page_size
"""

import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Extracts a page of data from the CSV file and returns it as a
        list of lists.

        Args:
            page (int, optional): The page number to retrieve. Defaults to 1.
            page_size (int, optional): The page size, i.e., the maximum number
            of items per page.
            Defaults to 10.

        Returns:
            List[List[str]]: A list of lists representing the extracted data
            page from the CSV file.

        Raises:
            AssertionError: If the 'page' or 'page_size' arguments are not
            positive integers.
        """
        assert isinstance(page, int) and isinstance(
            page_size, int)
        assert page > 0 and page_size > 0
        data = []
        with open('Popular_Baby_Names.csv') as file:
            csv_reader = csv.reader(file, delimiter=',')
            index = index_range(page, page_size)
            for pos, cv in enumerate(csv_reader):
                if pos in range(index[0] + 1, index[1] + 1):
                    data.append(cv)
        return data


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
