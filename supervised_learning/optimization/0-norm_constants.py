#!/usr/bin/env python3
"""
This module implements one function def normalization_constants(X).
"""
import numpy as np


def normalization_constants(X):
    """
    Function that calculates the normalization (standardization)
    constants of a matrix
    Args:
        X: a numpy.ndarray of shape (m, nx) to normalize,
        where x is the number of data points and nx is the number of features.
    Returns:
        The mean and standard deviation of each feature, respectively.
    """
    mean = np.mean(X, axis=0)
    std = np.std(X, axis=0)
    return mean, std
