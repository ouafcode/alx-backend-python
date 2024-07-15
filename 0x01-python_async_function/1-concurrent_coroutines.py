#!/usr/bin/env python3
""" The basics of async """

import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ multiple coroutines at the same time """
    lists = []
    for _ in range(n):
        delay = await(wait_random(max_delay))
        lists.append(delay)
    return sorted(lists)
