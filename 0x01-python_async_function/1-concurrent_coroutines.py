#!/usr/bin/env python3
""" The basics of async """

import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ multiple coroutines at the same time """
    lists = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delay = await asyncio.gather(*lists)
    return sorted(delay)
