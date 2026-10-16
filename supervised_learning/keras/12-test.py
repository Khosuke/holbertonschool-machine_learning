#!/usr/bin/env python3
"""
This module implements one function
def test_model(network, data, labels, verbose=True).
"""
import tensorflow.keras as K


def test_model(network, data, labels, verbose=True):
    """
    Function that tests a neural network.
    Args:
        network: The network model to test.
        data: The input data to test the model with.
        labels: The correct one-hot labels of data.
        verbose: Boolean that determines if output should be
            printed during the testing process.
    Returns:
        The loss and accuracy of the model with the testing data, respectively.
    """
    eval = network.evaluate(data, labels, verbose=verbose)
    return eval
