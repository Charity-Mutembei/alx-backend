#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import Dict, List


class Server:
    """
    code provided and copied
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """
        function I
        """
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """
        function II
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """
        function  III
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
        function IV
        """
        assert isinstance(index,
                          int) and 0 <= index < len(
                              self.indexed_dataset()
                              ), "Index out of range"
        assert isinstance(page_size, int
                          ) > 0, "Page size must be a positive integer"

        next_index = index + page_size
        data = [self.indexed_dataset().get(i) for i in range(
            index, next_index) if i in self.indexed_dataset()]

        return {
            "index": index,
            "page_size": page_size,
            "data": data,
            "next_index": next_index if next_index < len(
                self.indexed_dataset()) else None
        }
