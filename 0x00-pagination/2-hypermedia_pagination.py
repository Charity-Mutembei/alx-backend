#!/usr/bin/env python3
"""
Write a function named index_range that
takes two integer arguments page and page_size.
"""

import csv
import math
from typing import List, Dict, Union


def index_range(page: int, page_size: int) -> tuple:
    """
    Returns a tuple of size two containing a start
    index and an end index.
    """
    first_index = (page - 1) * page_size
    last_index = first_index + page_size
    return first_index, last_index


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List[str]]:
        """Cached dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip header
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List[str]]:
        """Return the appropriate page of dataset."""
        assert isinstance(page, int) and page > 0, "Page must be a positive integer."
        assert isinstance(page_size, int) and page_size > 0, "Page size must be a positive integer."

        dataset = self.dataset()
        start_index, end_index = index_range(page, page_size)

        if start_index >= len(dataset):
            return []

        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Union[int, List[List[str]], None]]:
        """Return a dictionary containing pagination details."""
        dataset = self.dataset()
        total_items = len(dataset)
        total_pages = math.ceil(total_items / page_size)

        # Use get_page to get the current page data
        current_page_data = self.get_page(page, page_size)

        # Calculate next and previous pages
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            'page_size': len(current_page_data),
            'page': page,
            'data': current_page_data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
