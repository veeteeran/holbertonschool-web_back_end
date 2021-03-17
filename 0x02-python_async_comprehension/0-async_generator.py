#!/usr/bin/env python3
"""Docstring for task 0"""
import asyncio
from random import uniform
from typing import Generator


async def async_generator() -> Generator[int, None, None]:
    """Yield a random number between 0 and 10"""
    for i in range(10):
        # random_val = uniform(0, 10)
        await asyncio.sleep(1)
        yield uniform(0, 10)
