#!/usr/bin/env python3
"""Docstring for task 1"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
        Returns the list of all the delays as floats

                Parameters:
                       n (int): the number of times to call wait_n
                       max_delay (int): max delay time passed to wait_random

                Returns:
                        A list of floats in ascending order
    """
    tasks = []
    for i in range(n):
        tasks.append(wait_random(max_delay))

    result = []
    for task in asyncio.as_completed(tasks):
        result.append(await task)

    return result
