#!/usr/bin/env python3
""" create a measure time function that returns the total execution time """


import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    measure the total execution time for wait_n(n, max_delay)
    and return total_time / n
    """
    s_time = time.time()
    asyncio.run(wait_n(n, max_delay))

    e_time = time.time()
    elapsed_time = e_time - s_time
    return elapsed_time / n
