#!/usr/bin/env python3
"""
This module implement one function mat_mul(mat1, mat2).
"""


def mat_mul(mat1, mat2):
    """
    Function that performs matrix multiplication.
    Args:
        mat1: first matrix.
        mat2: second matrix.
    """
    if len(mat1[0]) != len(mat2):
        return None

    result = []

    for i in range(len(mat1)):
        row = []

        for j in range(len(mat2[0])):
            value = 0

            for k in range(len(mat1[0])):
                value += mat1[i][k] * mat2[k][j]

            row.append(value)

        result.append(row)

    return result
