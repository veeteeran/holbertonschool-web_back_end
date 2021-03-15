#!/usr/bin/env python3
"""Docstring for task 6"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return sum of list as float. List contains integers and floats"""
    return sum(mxd_lst)
