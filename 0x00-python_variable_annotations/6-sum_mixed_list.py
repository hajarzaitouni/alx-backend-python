#!/usr/bin/env python3
"""
Define a module that calculate
the sum of a list containing both integers and floats.

Args:
    mxd_lst (List[Union[int, float]]): A list of integers and float numbers.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ returns the sum of elements of a list """
    return sum(mxd_lst)
