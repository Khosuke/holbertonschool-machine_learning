#!/usr/bin/env python3
"""
This script implement one function matrix_transpose
"""


def matrix_transpose(matrix):
    """
    Function that returns the transpose of a 2D matrix.
    Args:
        matrix: the matrix to transpose.
    """
    return [
        [matrix[j][i] for j in range(len(matrix))]
        for i in range(len(matrix[0]))
    ]
