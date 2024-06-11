#!/usr/bin/env python3
""" Import async_generator and create async_comprehension """

from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ return the 10 random numbers using async_generator """
    return [num async for num in async_generator()]
