#!/usr/bin/env python3
"""
Write a function named index_range that
takes two integer arguments page and page_size.
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Returns a tuple of size two containing a start
    index and an end index
    """
    first_index = (page - 1) * page_size
    last_index = first_index + page_size
    return first_index, last_index
