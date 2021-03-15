#!/usr/bin/env python3
"""Docstring for task 8"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a Callable, multiples multiplier by a float"""
    return lambda x: multiplier * 2.0
