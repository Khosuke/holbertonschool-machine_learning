#!/usr/bin/env python3
"""
This module implements one function def normalize(X, m, s).
"""


def normalize(X, m, s):
    """
    Function that normalizes (standardizes) a matrix
    Args:
        X: a numpy.ndarray of shape (d, nx) to normalize,
            where d is the number of data points,
            and nx is the number of features.
        m: a numpy.ndarray of shape (nx,) that contains
            the mean of all features of X.
        s: a numpy.ndarray of shape (nx,) that contains
            the standard deviation of all features of X.
    Returns:
        The normalized X matrix
    """
    return (X - m) / s
