#!/usr/bin/env python3
"""10. Duck typing - first element of a sequence"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    :param: lst type of Sequence[Any]
    :return: Any or None
    """
    if lst:
        return lst[0]
    else:
        return None
