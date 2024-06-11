#!/usr/bin/env python3
""" Measure runtime of async_comprehension executed in parallel """

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    execute async_comprehension 4 times in parallel using asyncio.gather,
    and return the total runtime.
    """
    st_time = time.time()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())

    end_time = time.time()
    elapsed_time = end_time - st_time

    return elapsed_time
