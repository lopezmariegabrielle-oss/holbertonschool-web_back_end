#!/usr/bin/env python3
"""
Task 0: Async Generator
"""
import asyncio
import random


async def async_generator():
    """
    Loop 10 times, wait 1 second, then yield a random number.
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
