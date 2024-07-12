#!/usr/bin/env python3
""" Complex types - functions """

from typing import Union, Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Complex types - functions

    Args:
       multiplier (float) : first arg.

    Returns:
       function : function that multiplies a float by multiplier.
    """
    def mult(m: float) -> float:
        """Func doc"""
        return m * multiplier

    return mult
