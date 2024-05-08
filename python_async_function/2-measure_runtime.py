#!/usr/bin/env python3
"""
Create a measure_time function with integers n
and max_delay as arguments that measures the total execution time for wait_n
(n, max_delay), and returns total_time / n.
Your function should return a float.
"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the average time taken per task to complete.

    Args:
        n (int): The number of tasks to execute.
        max_delay (int): The maximum delay time for each task.

    Returns:
        float: The average time taken per task to complete.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    elapsed_time = time.time() - start_time
    return elapsed_time / n
