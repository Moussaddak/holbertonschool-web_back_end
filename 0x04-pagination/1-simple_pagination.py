#!/usr/bin/env python3
""" 1. Simple pagination """
import csv
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return a tuple of size two containing a start index and an end index.
    """
    start_idx, end_idx = page * page_size, page * page_size
    return start_idx - page_size, end_idx


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
        """
        takes two arguments page with default value 1 and page_size with 10.
        """
        assert (type(page) is int and type(page_size) is int)
        assert (page > 0 and page_size > 0)

        index = index_range(page, page_size)
        self.dataset()
        if len(self.__dataset) > index[0]:
            return self.__dataset[index[0]:index[1]]
        return []
