#!/usr/bin/env python3
"""
This module implements one function def predict(network, data, verbose=False)
"""
import tensorflow.keras as K


def predict(network, data, verbose=False):
    """
    Function that makes a prediction using a neural network.
    Args:
        network: The network model to make the prediction with
        data: The input data to make the prediction with
        verbose: Boolean that determines if output should be
            printed during the prediction process
    Returns:
        The prediction for the data.
    """
    pred = network.predict(data, verbose=verbose)
    return pred
