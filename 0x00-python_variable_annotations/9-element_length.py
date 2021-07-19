#!/usr/bin/env python3
"""9. Let's duck type an iterable object"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    :param lst: list of items
    :return: list of tuples
    """
    return [(i, len(i)) for i in lst]
