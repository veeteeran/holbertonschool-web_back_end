#!/usr/bin/env python3
"""Docstring for task 1"""
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
        Collect 10 random numbers using an async comprehensing over
        async_generator. Return the 10 random numbers
    """
    return [number async for number in async_generator()]
