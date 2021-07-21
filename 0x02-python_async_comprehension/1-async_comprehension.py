#!/usr/bin/env python3
"""1. Async Comprehensions"""

import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Tasks
    """
    return [num async for num in async_generator()]
