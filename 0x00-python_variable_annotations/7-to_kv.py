#!/usr/bin/env python3
""" Complex types -  string and int/float to tuple """

from typing import List, Union, Tuple


def to_kv(k: str, v: List[Union[int, float]]) -> Tuple[str, float]:
    """
    string and int/float to tuple

    Args:
       v (list[int, float]) : list of int and floats.
       k (string) : the first element str.

    Returns:
       tuple : return tuple of string and float.
    """
    return (k, float(v ** 2))
