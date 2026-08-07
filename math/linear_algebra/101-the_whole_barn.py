#!/usr/bin/env python3
"""
This module implement one function def add_matrices(mat1, mat2)
"""


def add_matrices(mat1, mat2):
    """
    Function
    Args:
        mat1:
        mat2:
    """
    if not isinstance(mat1, list) and not isinstance(mat2, list):
        return mat1 + mat2

    if ((isinstance(mat1, list) and not isinstance(mat2, list)) or
            (not isinstance(mat1, list) and isinstance(mat2, list))):
        return None

    if len(mat1) != len(mat2):
        return None

    new_matrix = []
    for i in range(len(mat1)):
        result = add_matrices(mat1[i], mat2[i])
        if result is None:
            return None
        else:
            new_matrix.append(result)
    return new_matrix
