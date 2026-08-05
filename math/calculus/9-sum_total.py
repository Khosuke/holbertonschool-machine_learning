#!/usr/bin/env python3
"""
This module implements one function def summation_i_squared(n)
"""


def summation_i_squared(n):
    """
    Function that calculates the sum of
    the first n consecutive square numbers
    Args:
        n: the stopping condition number
    """
    if not isinstance(n, int):
        return None
    if n <= 0:
        return None
    return int((n*(n+1)*(2*n+1))/6)
