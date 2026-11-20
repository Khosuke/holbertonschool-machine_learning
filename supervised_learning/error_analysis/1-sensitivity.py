#!/usr/bin/env python3
"""
This module implements one function
def sensitivity(confusion)
"""
import numpy as np


def sensitivity(confusion):
    """
    Function that calculates the sensitivity for each class
    in a confusion matrix.
    Args:
        confusion: is a confusion numpy.ndarray of shape (classes, classes)
            where row indices represent the correct labels and column
            indices represent the predicted labels.
            classes is the number of classes.
    Returns:
        a numpy.ndarray of shape (classes,) containing the sensitivity
        of each class.
    """
    return np.divide(np.diag(confusion), confusion.sum(axis=1))
