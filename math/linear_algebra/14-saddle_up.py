#!/usr/bin/env python3
"""
This module implements one function def np_matmul(mat1, mat2)
"""
import numpy as np


def np_matmul(mat1, mat2):
    """
    Function that performs matrix multiplication
    Args:
        mat1: first matrix to multiply
        mat2: second matrix to multiply
    """
    return mat1.__matmul__(mat2)
