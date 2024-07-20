#!/usr/bin/env python3
"""
1. Simple pagination
"""
import csv
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """
    Returns a tuple of size two containing a start
    index and an end index
    """
    first_index = (page - 1) * page_size
    last_index = first_index + page_size
    return first_index, last_index


class Server:
    """
    copied class
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        assert isinstance(page,
                          int) and page > 0, "must be positive integer"
        assert isinstance(page_size,
                          int) > 0, "must be positive integer"

        first_index, last_index = index_range(page, page_size)
        dataset = self.dataset()

        if first_index >= len(dataset):
            return []

        return dataset[first_index:last_index]
