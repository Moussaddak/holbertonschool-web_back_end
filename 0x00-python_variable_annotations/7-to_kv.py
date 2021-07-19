#!/usr/bin/env python3
"""7. Complex types - string and int/float to tuple"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str,float]:
    """
    function take two args, 1st str and 2nd int or float
    and return tuple
    """
    return (k, v)
