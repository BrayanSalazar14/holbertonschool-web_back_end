#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Retrieves a paginated subset of indexed data with hypermedia links.

        Args:
            index (int, optional): The starting index of the subset.
            Defaults to None.
            page_size (int, optional): The number of items per page.
            Defaults to 10.

        Returns:
            dict: A dictionary containing a paginated subset of indexed data
            along with hypermedia links.
                - "index" (int): The starting index of the subset.
                - "data" (list): The list of items for the current page.
                - "page_size" (int): The number of items per page.
                - "next_index" (int): The index of the next page.

        Raises:
            AssertionError: If the provided index exceeds the total
            number of indexed pages.

        Notes:
            The indexed dataset must be accessible through the method
            'indexed_dataset()'.
            This function retrieves a subset of data starting from
            the specified index
            and ending at the next index after 'page_size' elements.
        """
        total_pages = len(self.indexed_dataset())
        assert index <= total_pages
        index_dataset = self.indexed_dataset()
        next_index = index + page_size
        if index not in index_dataset.keys():
            next_index += 1
        data = [dt for pos, dt in index_dataset.items() if pos in range(
            index, next_index)]
        data_page = {
            "index": index,
            "data": data,
            "page_size": page_size,
            "next_index": next_index
        }
        return data_page
