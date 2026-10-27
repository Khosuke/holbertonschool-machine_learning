#!/usr/bin/env python3
"""
This module implements one function
def update_variables_momentum(alpha, beta1, var, grad, v)
"""
import numpy as np


def update_variables_momentum(alpha, beta1, var, grad, v):
    """
    Function that updates a variable using the gradient descent
    with momentum optimization algorithm.
    Args:
        alpha: is the learning rate.
        beta1: is the momentum weight.
        var: a numpy.ndarray containing the variable to be updated.
        grad: a numpy.ndarray containing the gradient of var.
        v: is the previous first moment of var.
    Returns:
        the updated variable and the new moment, respectively.
    """
    new_v = beta1 * v + (1 - beta1) * grad
    new_var = var - alpha * new_v
    return new_var, new_v
