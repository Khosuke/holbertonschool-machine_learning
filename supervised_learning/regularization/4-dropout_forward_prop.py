#!/usr/bin/env python3
"""
This module implements one function
def dropout_forward_prop(X, weights, L, keep_prob)
"""
import numpy as np


def dropout_forward_prop(X, weights, L, keep_prob):
    """
    Function that conducts forward propagation using Dropout.
    All layers except the last use the tanh activation function.
    The last layer uses the softmax activation function.
    Args:
        X: is a numpy.ndarray of shape (nx, m) containing the input data
            for the network.
            nx is the number of input features.
            m is the number of data points.
        weights: is a dictionary of the weights and biases of the
            neural network.
        L: is the number of layers in the network.
        keep_prob: is the probability that a node will be kept.
    Returns:
        a dictionary containing the outputs of each layer and the
        dropout mask used on each layer.
    """
    cache = {"A0": X}

    for layer in range(1, L + 1):
        prev_output = cache[f"A{layer - 1}"]
        l_weights = weights[f"W{layer}"]
        l_bias = weights[f"b{layer}"]

        z = np.matmul(l_weights, prev_output) + l_bias

        if layer == L:
            exp_z = np.exp(z)
            output = exp_z / np.sum(exp_z, axis=0, keepdims=True)
        else:
            output = np.tanh(z)
            dropout_mask = np.random.binomial(1, keep_prob,
                                              size=output.shape)
            output = output * dropout_mask / keep_prob
            cache[f"D{layer}"] = dropout_mask

        cache[f"A{layer}"] = output

    return cache
