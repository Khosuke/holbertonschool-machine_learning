#!/usr/bin/env python3
"""
This module implements one function def one_hot()
"""
import tensorflow.keras as K


def one_hot(labels, classes=None):
    """
    Function that converts a label vector into a one-hot matrix
    Args:
        labels:
        classes:
    Returns:
        The one-hot matrix
    """
    return K.utils.to_categorical(labels, classes)
