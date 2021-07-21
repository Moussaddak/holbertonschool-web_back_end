#!/usr/bin/env python3
"""0. The basics of async"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Tasks
    """
    timeToSleep = random.uniform(0, max_delay)
    await asyncio.sleep(timeToSleep)
    return timeToSleep
