#!/usr/bin/env python3
"""
This module implements one function def shuffle_data(X, Y)
"""
import numpy as np


def shuffle_data(X, Y):
    """
    Function that shuffles the data points in two matrices the same way
    Args:
        X is the first numpy.ndarray of shape (m, nx) to shuffle
            where m is the number of data points
            and nx is the number of features in X.
        Y is the second numpy.ndarray of shape (m, ny) to shuffle
            where m is the same number of data points as in X
            and ny is the number of features in Y.
    Returns:
        the shuffled X and Y matrices.
    """
    return np.random.permutation(X), np.random.permutation(Y)
