#!/usr/bin/env python3
"""
Ce module fournit un générateur asynchrone.
"""
import asyncio
import random


async def async_generator():
    """
    Coroutine qui attend 1 seconde et produit un nombre aléatoire 10 fois.
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
