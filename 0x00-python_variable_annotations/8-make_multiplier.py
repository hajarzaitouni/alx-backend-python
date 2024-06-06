#!/usr/bin/env python3
"""
function that takes a float multiplier as argument
and returns a function that multiplies a float by multiplier

Args:
    multiplier (float): float
"""

from typing import Callable


def make_multiplier(multiplier: float, ) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by the given multiplier.
    """
    return lambda x: x * multiplier
