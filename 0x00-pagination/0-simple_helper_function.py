#!/usr/bin/env python3
"""
Write a function named index_range that
takes two integer arguments page and page_size.
"""


def index_range(page, page_size):
    """
    function index_range
    """
    if page < 1 or page_size < 1:
        raise ValueError("Both must be positive integers.")

    start_index = (page - 1) * page_size
    end_index = start_index + page_size - 1
    
    return (start_index, end_index)
