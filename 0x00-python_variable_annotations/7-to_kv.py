#!/usr/bin/env python3
"""Docstring for task 7"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple. Values of tuple are k, v squared"""
    return (k, v * v)
