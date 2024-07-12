#!/usr/bin/env python3
""" Complex types - list of floats """

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    lists of floats

    Args:
       input_list (list[float]) : list of floats.

    Returns:
       float : return sum of floats.
    """
    val: float = 0
    for i in input_list:
        val += i
    return val
