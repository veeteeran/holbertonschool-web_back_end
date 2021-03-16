#!/usr/bin/env python3
"""Docstring for task 3"""
import asyncio
from typing import Callable
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Callable:
    """
        Returns a asyncio.Task

                Parameter:
                       max_delay (int): max delay time passed to wait_random

                Returns:
                        asyncio.Task
    """
    return asyncio.create_task(wait_random(max_delay))
