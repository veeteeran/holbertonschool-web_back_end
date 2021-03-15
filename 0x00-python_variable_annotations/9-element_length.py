#!/usr/bin/env python3
"""Docstring for task 9"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Not sure I understand the point of this"""
    return [(i, len(i)) for i in lst]
