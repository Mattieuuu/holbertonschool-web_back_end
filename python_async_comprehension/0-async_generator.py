#!/usr/bin/env python3
"""
Module contenant un générateur asynchrone qui crée des nombres aléatoires.
"""

import asyncio
import random
from typing import AsyncGenerator  # Changement ici : AsyncGenerator au lieu de Generator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Générateur magique qui donne 10 nombres au hasard,
    en faisant une pause d'1 seconde entre chaque nombre.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)