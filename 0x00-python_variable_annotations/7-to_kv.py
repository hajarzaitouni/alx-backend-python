#!/usr/bin/env python3
"""
Returns a tuple where the first element is the string k,
and the second element is the square of the int/float v

Args:
    k (str): A string.
    v (Union[int, float]): An integer or float number.
"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Return tuple consisting of k and the square of v """
    return (k, float(v ** 2))
