#!/usr/bin/env python3
"""
This module implements one function def poly_integral(poly, C=0)
"""


def poly_integral(poly, C=0):
    """
    Function that calculates the integral of a polynomial
    Args:
        poly: list of coefficients representing a polynomial
        C: integer representing the integration constant
            default is 0
    """
    if (not isinstance(poly, list) or len(poly) == 0):
        return None

    if not all(isinstance(x, (int, float)) for x in poly):
        return None

    if not isinstance(C, (int, float)) or C is None:
        return None

    if poly == [0]:
        return [C]

    result = [
        C if i == 0 else poly[i - 1] / i
        for i in range(len(poly) + 1)
    ]

    return [
        int(x) if isinstance(x, float) and x.is_integer() else x
        for x in result
    ]
