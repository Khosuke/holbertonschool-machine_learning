#!/usr/bin/env python3
"""
This module implements one function def np_cat(mat1, mat2, axis=0).
"""
import numpy as np


def np_cat(mat1, mat2, axis=0):
    """
    Function that concatenates two matrices along a specific axis
    Args:
        mat1: first matrix.
        mat2: second matrix.
        axis: the axis, default is 0.
    """
    return np.concatenate((mat1, mat2), axis)
