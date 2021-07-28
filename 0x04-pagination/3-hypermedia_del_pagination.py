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
            :param index:
            :param page_size:
            :return: dict
            """
        assert type(index) is int and type(page_size) is int
        assert 0 <= index < len(self.indexed_dataset())

        idx = self.__indexed_dataset
        r = []
        [r.append((i, idx[i])) for i in range(index, len(self.__dataset))
         if i in idx and len(r) < page_size]
        return {
            'index': index,
            'data': [i[1] for i in r],
            'page_size': len(r),
            'next_index': max([i[0] for i in r]) + 1
        }
