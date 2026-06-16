#!/usr/bin/env python3
"""
Ce module fournit une coroutine asynchrone simple pour expérimenter
les bases du fonctionnement de asyncio et des délais aléatoires.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Attend un délai aléatoire entre 0 et max_delay secondes,
    puis retourne ce délai.
    """
    random.uniform(0, max_delay)
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
