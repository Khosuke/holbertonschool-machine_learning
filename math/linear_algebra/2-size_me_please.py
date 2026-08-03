#!/usr/bin/env python3
"""
This script implement one function matrix_shape
"""

def matrix_shape(matrix):
    """
    Function that calculates the shape of a matrix.
    Args:
        matrix: the matrix we want to calculate the shape of.
    """
    if not isinstance(matrix, list):
        """
        
        """
        return []
    return [len(matrix)] + matrix_shape(matrix[0])
