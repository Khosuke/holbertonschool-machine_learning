#!/usr/bin/env python3
"""
This module implements one function
def l2_reg_gradient_descent(Y, weights, cache, alpha, lambtha, L)
"""
import numpy as np


def l2_reg_gradient_descent(Y, weights, cache, alpha, lambtha, L):
    """
    Function that updates the weights and biases of a neural network
    using gradient descent with L2 regularization.
    The neural network uses tanh activations on each layer except the
    last, which uses a softmax activation.
    The weights and biases of the network are updated in place.
    Args:
        Y: is a one-hot numpy.ndarray of shape (classes, m) that contains
            the correct labels for the data.
            classes is the number of classes.
            m is the number of data points.
        weights: is a dictionary of the weights and biases of the
            neural network.
        cache: is a dictionary of the outputs of each layer of the
            neural network.
        alpha: is the learning rate.
        lambtha: is the L2 regularization parameter.
        L: is the number of layers of the network.
    Returns:
        None, the weights and biases are updated in place.
    """
    m = Y.shape[1]
    l_error = cache[f"A{L}"] - Y

    for layer in range(L, 0, -1):
        prev_output = cache[f"A{layer - 1}"]
        l_weights = weights[f"W{layer}"]
        l_bias = weights[f"b{layer}"]

        l2_penalty = (lambtha / m) * l_weights
        weights_grad = (1 / m) * np.matmul(l_error, prev_output.T) + l2_penalty
        bias_grad = (1 / m) * np.sum(l_error, axis=1, keepdims=True)

        tanh_derivative = 1 - (prev_output ** 2)
        l_error = (np.matmul(l_weights.T, l_error)) * tanh_derivative

    weights[f"W{layer}"] = l_weights - alpha * weights_grad
    weights[f"b{layer}"] = l_bias - alpha * bias_grad
