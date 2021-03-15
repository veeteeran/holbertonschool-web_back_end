#!/usr/bin/env python3
"""Docstring for task 10"""
from typing import Any, Sequence, Union


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Augmented code above with correct duck-typed annotations"""
    if lst:
        return lst[0]
    else:
        return None
