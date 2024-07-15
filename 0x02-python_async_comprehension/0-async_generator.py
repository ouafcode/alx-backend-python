#!/usr/bin/env python3
""" docs funct """

import asyncio
import random


async def async_generator() -> float:
    """ Async Generator """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
