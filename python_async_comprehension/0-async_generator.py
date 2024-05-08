#!/usr/bin/env python3
"""
The coroutine will loop 10 times, each time asynchronously wait 1 second,
then yield a random number between 0 and 10. Use the random module.
"""
import asyncio
from random import uniform


async def async_generator():
    """
    Asynchronous generator that yields random floats between 0 and 10
    with a delay of 1 second between each yield.

    Yields:
        float: A random float between 0 and 10.

    Raises:
        None

    Usage:
        async for number in async_generator():
            print(number)
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)
