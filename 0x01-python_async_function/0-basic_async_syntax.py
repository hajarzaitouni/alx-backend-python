#!/usr/bin/env python3
""" Define an asynchronous coroutine """

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ wait for a rendom delay and return it """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
