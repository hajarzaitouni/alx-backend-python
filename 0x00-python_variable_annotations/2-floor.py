#!/usr/bin/env python3
"""
Returns the largest integer less than
or equal to a given float number
"""


def floor(n: float) -> int:
    """ returns the largest integer less than or equal to n"""
    return int(n) if n >= 0 else int(n) - 1
