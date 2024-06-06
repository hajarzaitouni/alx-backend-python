#!/usr/bin/env python3
"""
adding type annotations to the function below
"""

from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """ Returns the dictionary value if it exists """
    if key in dct:
        return dct[key]
    else:
        return default
