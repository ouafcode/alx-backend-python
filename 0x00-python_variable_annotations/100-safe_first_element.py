#!/usr/bin/env python3
""" Module documentation """
from typing import List, Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ Duck typing - first element of a sequence """
    if lst:
        return lst[0]
    else:
        return None
