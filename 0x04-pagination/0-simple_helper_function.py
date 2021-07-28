#!/usr/bin/env python3
""" 0. Simple helper function """
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return a tuple of size two containing a start index and an end index.
    """
    start_idx, end_idx = page * page_size, page * page_size
    return start_idx - page_size, end_idx
