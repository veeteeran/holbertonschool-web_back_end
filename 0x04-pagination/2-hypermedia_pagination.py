#!/usr/bin/env python3
"""Index range module"""
import csv
import math
from typing import Dict, List, Tuple


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
        """Paginate and return the appropriate page of the dataset
           (i.e. the correct list of rows)

                Return empty list if input arguments are out of range
                for the dataset
        """
        assert type(page) is int and type(page_size) is int
        assert page > 0 and page > 0

        self.dataset()

        if page * page_size > len(self.__dataset):
            return []

        result = index_range(page, page_size)

        data = [self.__dataset[i] for i in range(result[0], result[1])]

        return data

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Returns a dictionary containing key-value pairs:
                page_size: the length of the returned dataset page
                page: the current page number
                data: the dataset page from get_page
                next_page: next page number, None if no next page
                prev_page: previous page number, None if no previous page
                total_pages: total number of pages in the dataset as an int
        """
        data = self.get_page(page, page_size)
        total_pages = round(len(self.__dataset) / page_size)

        size = page_size

        if page + 1 < total_pages:
            next_page = page + 1
        else:
            next_page = None

        if page == 1:
            prev_page = None
        else:
            prev_page = page - 1

        if data == []:
            size = 0
            next_page = None
            prev_page = page - 1
            total_pages = math.floor(len(self.__dataset) / page_size) + 1

        returnDict = {'page_size': size, 'page': page, 'data': data,
                      'next_page': next_page, 'prev_page': prev_page,
                      'total_pages': total_pages}

        return returnDict
