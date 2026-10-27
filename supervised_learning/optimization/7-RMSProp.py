#!/usr/bin/env python3
"""
This module implements one function
def update_variables_RMSProp(alpha, beta2, epsilon, var, grad, s)
"""
import numpy as np


def update_variables_RMSProp(alpha, beta2, epsilon, var, grad, s):
    """
    Function that updates a variable using the RMSProp
    optimization algorithm.
    Args:
        alpha: is the learning rate.
        beta2: is the RMSProp weight.
        epsilon: is a small number to avoid division by zero.
        var: a numpy.ndarray containing the variable to be updated.
        grad: a numpy.ndarray containing the gradient of var.
        s: is the previous second moment of var.
    Returns:
        the updated variable and the new moment, respectively.
    """
    new_s = beta2 * s + (1 - beta2) * grad**2
    new_var = var - alpha * grad / (np.sqrt(new_s) + epsilon)
    return new_var, new_s
