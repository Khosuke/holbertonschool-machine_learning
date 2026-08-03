#!/usr/bin/env python3
"""
This module implement one function np_elementwise(mat1, mat2)
"""
import numpy as np


def np_elementwise(mat1, mat2):
    """
    Function that performs element-wise addition, subtraction,
    multiplication, and division.
    Args:
        mat1: first matrix used to perform operation
        mat2: second matrix used to perform operation
    """
    return np.ndarray.__add__(mat1, mat2), \
        np.ndarray.__sub__(mat1, mat2), \
        np.ndarray.__mul__(mat1, mat2), \
        np.ndarray.__truediv__(mat1, mat2)
