#!/usr/bin/env python3
"""
Ce module contient une coroutine qui exécute plusieurs tâches
asynchrones de manière concurrente.
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Exécute wait_random n fois avec le max_delay spécifié
    et retourne la liste des délais par ordre croissant.
    """
    delays: List[float] = []
    taches = [wait_random(max_delay) for _ in range(n)]

    for tache_terminee in asyncio.as_completed(taches):
        delay = await tache_terminee
        delays.append(delay)

    return delays
