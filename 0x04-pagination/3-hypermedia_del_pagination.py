#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import Dict, List


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
        """Return a diction of hyper indexed data"""
        assert index < len(self.__indexed_dataset)

        start = index
        end = index + page_size
        next_index = end

        if self.__indexed_dataset.get(index) is None:
            offset = len(self.__dataset) - len(self.__indexed_dataset)
            start = index + offset
            end += 1
            next_index += 1

        data = [self.__indexed_dataset[i] for i in range(start, end)]

        output = {'index': index, 'next_index': next_index,
                  'page_size': page_size, 'data': data}

        return output
