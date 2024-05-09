#!/usr/bin/env python3
"""
measure_runtime should measure the total runtime and return it.
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure the total runtime for executing async_comprehension
    four times concurrently.

    Returns:
        float: The total runtime in seconds.

    Usage:
        total_runtime = await measure_runtime()
    """
    start_time = time.time()
    result = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*result)
    return time.time() - start_time
