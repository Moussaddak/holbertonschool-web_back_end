#!/usr/bin/env python3
"""2. Run time for four parallel comprehensions"""
import time
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Tasks
    """
    start = time.time()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    return time.time() - start
