#!/usr/bin/env python3
"""
This module implements one function
def f1_score(confusion)
It relies on the sensitivity and precision functions created previously
in 1-sensitivity.py and 2-precision.py.
"""
import numpy as np
sensitivity = __import__('1-sensitivity').sensitivity
precision = __import__('2-precision').precision


def f1_score(confusion):
    """
    Function that calculates the F1 score of a confusion matrix.
    The F1 score of each class combines its sensitivity and its precision.
    Args:
        confusion: is a confusion numpy.ndarray of shape (classes, classes)
            where row indices represent the correct labels and column
            indices represent the predicted labels.
            classes is the number of classes.
    Returns:
        a numpy.ndarray of shape (classes,) containing the F1 score
        of each class.
    """
    sens = sensitivity(confusion)
    prec = precision(confusion)
    return np.divide(np.multiply(2, np.multiply(prec, sens)), np.add(prec, sens))
