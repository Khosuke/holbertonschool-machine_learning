#!/usr/bin/env python3
"""
This module implement one function def np_slice(matrix, axes={})
"""


def np_slice(matrix, axes={}):
    """
    Function that slices a matrix along specific axes
    Args:
        matrix: the matrix to slice
        axes: the specified axes
    """

    slices = [slice(None)] * matrix.ndim

    for axis, s in axes.items():
        if len(s) == 1:
            slices[axis] = s[0]
        else:
            slices[axis] = slice(*s)

    return matrix[tuple(slices)]
