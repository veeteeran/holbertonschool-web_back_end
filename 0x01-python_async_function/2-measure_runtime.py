#!/usr/bin/env python3
"""Docstring for task 2"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
        Returns time elapsed in execution of function

                Parameters:
                       n (int): the number of times to call wait_n
                       max_delay (int): max delay time passed to wait_n

                Returns:
                        total_time / n as a float
    """
    start = time.time()

    asyncio.run(wait_n(n, max_delay))

    end = time.time()

    return (end - start) / n
