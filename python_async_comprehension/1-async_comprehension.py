#!/usr/bin/env python3
"""
The coroutine will collect 10 random numbers
using an async comprehensing over async_generator,
then return the 10 random numbers.
"""
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Asynchronous comprehension that awaits values from an
    async generator and returns them as a list.

    Returns:
        List[float]: A list of floating-point numbers
        obtained from the async generator.

    Usage:
        result = await async_comprehension()
    """
    return [item async for item in async_generator()]
