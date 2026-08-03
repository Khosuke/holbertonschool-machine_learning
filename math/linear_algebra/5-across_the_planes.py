#!/usr/bin/env python3
"""
This module implement one function add_matrices2D(mat1, mat2).
"""


def add_matrices2D(mat1, mat2):
    """
    Function that adds two matrices element-wise.
    Args:
        mat1: first matrix to add.
        mat2: second matrix to add.
    """
    if (len(mat1) != len(mat2) or
            len(mat1[0]) != len(mat2[0])):
        return None
    return [
        [mat1[i][j]+mat2[i][j] for j in range(len(mat1))]
        for i in range(len(mat1))
    ]
