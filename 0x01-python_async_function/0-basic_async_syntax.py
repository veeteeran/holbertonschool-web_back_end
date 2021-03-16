#!/usr/bin/env python3
"""Docstring for task 0"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Return a random delay between 0 and max_delay inclusive"""
    random_val = random.uniform(0, max_delay)
    await asyncio.sleep(random_val)
    return random_val
