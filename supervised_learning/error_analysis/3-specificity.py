#!/usr/bin/env python3
"""
This module implements one function
def specificity(confusion)
"""
import numpy as np


def specificity(confusion):
    """
    Function that calculates the specificity for each class
    in a confusion matrix.
    Args:
        confusion: is a confusion numpy.ndarray of shape (classes, classes)
            where row indices represent the correct labels and column
            indices represent the predicted labels.
            classes is the number of classes.
    Returns:
        a numpy.ndarray of shape (classes,) containing the specificity
        of each class.
    """
    total = confusion.sum()
    row = confusion.sum(axis=1)
    column = confusion.sum(axis=0)
    diagonal = np.diag(confusion)

    tn = np.add(np.subtract(np.subtract(total, row), column), diagonal)
    fp = np.subtract(column, diagonal)
    return np.divide(tn, np.add(tn, fp))
