#!/usr/bin/env python3
"""Index range module"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
        Return tuple of size two containing a start index and an end index
        corresponding to the range of indexes to return in a list for those
        particular pagination parameters

            Parameters:
                    page(int): page number
                    page_size(int): items on each page

            Return:
                    A tuple of the start index and end index
    """
    start = (page * page_size) - page_size
    end = page * page_size

    return (start, end)
