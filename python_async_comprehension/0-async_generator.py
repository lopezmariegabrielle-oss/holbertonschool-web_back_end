#!/usr/bin/env python3
"""
This module provides an asynchronous generator coroutine.
"""
import asyncio
import random


async def async_generator():
    """
    Asynchronous generator that loops 10 times.

    Each iteration asynchronously waits for 1 second,
    then yields a random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
