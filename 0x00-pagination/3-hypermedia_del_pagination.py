#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict, Union


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List[str]]:
        """Cached dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip header

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List[str]]:
        """Dataset indexed by sorting position, starting at 0."""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(
        self, index: int = None, page_size: int = 10
    ) -> Dict[str, Union[int, List[List[str]], None]]:
        """Return a dictionary with pagination details including deletion
        resilience.
        """
        assert index is None or (
            isinstance(index, int) and 0 <= index < len(self.__indexed_dataset)
        ), "Index is out of range."
        assert isinstance(page_size, int
                          ) and page_size > 0, "must be positive."

        indexed_dataset = self.indexed_dataset()
        data = []
        current_index = index
        start_index = index

        while len(data) < page_size and current_index in indexed_dataset:
            data.append(indexed_dataset[current_index])
            current_index += 1

        next_index = current_index if len(data) == page_size else None

        return {
            'index': start_index,
            'data': data,
            'page_size': page_size,
            'next_index': next_index
        }
