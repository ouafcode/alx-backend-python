#!/usr/bin/env python3
""" Complex types -  string and int/float to tuple """

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    string and int/float to tuple

    Args:
       v (list[int, float]) : list of int and floats.
       k (string) : the first element str.

    Returns:
       tuple : return tuple of string and float.
    """
    return (k, v ** 2)
