#!/usr/bin/env python3
"""
This module implement one function np_elementwise(mat1, mat2)
"""


def np_elementwise(mat1, mat2):
    """
    Function that performs element-wise addition, subtraction,
    multiplication, and division.
    Args:
        mat1: first matrix used to perform operation
        mat2: second matrix used to perform operation
    """
    return mat1.__add__(mat2), \
        mat1.__sub__(mat2), \
        mat1.__mul__(mat2), \
        mat1.__truediv__(mat2)
