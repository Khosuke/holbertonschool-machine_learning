#!/usr/bin/env python3
"""
This module implements one function
def create_mini_batches(X, Y, batch_size)
"""
shuffle_data = __import__('2-shuffle_data').shuffle_data


def create_mini_batches(X, Y, batch_size):
    """
    Function that creates mini-batches to be used for training
    a neural network using mini-batch gradient descent.
    Args:
        X: a numpy.ndarray of shape (m, nx) representing input data
            where m is the number of data points
            and nx is the number of features in X.
        Y: a numpy.ndarray of shape (m, ny) representing the labels
            where m is the same number of data points as in X
            and ny is the number of classes for classification tasks.
        batch_size: is the number of data points in a batch.
    Returns:
        a list of mini-batches containing tuples (X_batch, Y_batch).
    """
    X, Y = shuffle_data(X, Y)

    mini_batch = []
    for i in range(0, len(X), batch_size):
        mini_batch.append((X[i:i + batch_size], Y[i:i + batch_size]))

    return mini_batch
