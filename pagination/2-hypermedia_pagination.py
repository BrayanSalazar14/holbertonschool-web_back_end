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
        with open('Popular_Baby_Names.csv') as file:
            csv_reader = csv.reader(file, delimiter=',')
            index = index_range(page, page_size)
            data = [cv for pos, cv in enumerate(csv_reader)
                    if pos in range(index[0] + 1, index[1] + 1)]
        return data

    def get_hyper(self, page, page_size):
        """
        Generates a paginated data response with hypermedia links.

        Args:
            page (int): The current page number.
            page_size (int): The number of items per page.

        Returns:
            dict: A dictionary containing paginated data along with
            hypermedia links.
                - "page_size" (int): The number of items per page.
                - "page" (int): The current page number.
                - "data" (list): The list of items for the current page.
                - "next_page" (int or None): The number of the next page or
                None if it doesn't exist.
                - "prev_page" (int or None): The number of the previous page or
                None if it doesn't exist.
                - "total_pages" (int): The total number of pages.

        Notes:
            If there are additional elements that do not fill a complete page,
            an additional page is needed to display them.
        """
        index = index_range(page, page_size)
        total_pages = len(self.dataset())
        data_pages = {
            "page_size": page_size,
            "page": page,
            "data": self.get_page(page, page_size),
            "next_page": page + 1,
            "prev_page": page - 1,
            "total_pages": total_pages // page_size
        }
        if index[1] > total_pages:
            data_pages['page_size'] = 0
            data_pages['next_page'] = None

        if data_pages['prev_page'] == 0:
            data_pages['prev_page'] = None

        if total_pages % page_size > 0:
            """
            Si es mayor a 0 significa que hay elementos adicionales
            que no llenan una pagina completa, asi que necesitamos
            una pagina adicional para mostrar los elementos adicionales
            """
            data_pages['total_pages'] += 1
        return data_pages


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
