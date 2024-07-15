#!/usr/bin/env python3
""" docs funct """
from typing import List
import asyncio

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ Async Comprehensions """
    return [item async for item in async_generator()]
