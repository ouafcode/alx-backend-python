#!/usr/bin/env python3
""" Complex types - mixed list """

from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """
    lists mixed of int and float

    Args:
       mxd_list (list[int, float]) : list of int and floats.

    Returns:
       float : return sum of floats.
    """
    val: float = 0
    for i in mxd_list:
        val += i
    return val
