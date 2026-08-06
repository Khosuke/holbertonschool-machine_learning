#!/usr/bin/env python3
"""
This module implements one function def poly_derivative(poly)
"""

def poly_derivative(poly):
    """
    function that calculates the derivative of a polynomial
    Args:
        poly: list of coefficients representing a polynomial
    """
    if (not isinstance(poly, list) or len(poly) == 0):
        return None

    if not all(isinstance(x, (int, float)) for x in poly):
        return None

    if len(poly) == 1:
        return [0]

    return [poly[i] * i for i in range(1, len(poly))]
