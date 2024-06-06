#!/usr/bin/env python3
"""
Annotate the below function's
"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    returns the first element of a list if there is any,
    otherwise None
    """
    if lst:
        return lst[0]
    else:
        return None
