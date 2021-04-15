#!/usr/bin/env python3
"""main file"""
from utils import access_nested_map


nested_map = {"a": {"b": {"c": 1}}}
access_nested_map(nested_map, ["a", "b", "c"])
