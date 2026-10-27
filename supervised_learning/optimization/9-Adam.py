#!/usr/bin/env python3
"""
This module implements one function
def update_variables_Adam(alpha, beta1, beta2, epsilon, var, grad, v, s, t)
"""
import numpy as np


def update_variables_Adam(alpha, beta1, beta2, epsilon, var, grad, v, s, t):
    """
    Function that updates a variable in place using the Adam
    optimization algorithm.
    Args:
        alpha: is the learning rate.
        beta1: is the weight used for the first moment.
        beta2: is the weight used for the second moment.
        epsilon: is a small number to avoid division by zero.
        var: a numpy.ndarray containing the variable to be updated.
        grad: a numpy.ndarray containing the gradient of var.
        v: is the previous first moment of var.
        s: is the previous second moment of var.
        t: is the time step used for bias correction.
    Returns:
        the updated variable, the new first moment,
        and the new second moment, respectively.
    """
    new_v = beta1 * v + (1 - beta1) * grad
    new_s = beta2 * s + (1 - beta2) * grad**2
    v_cor = new_v / (1 - beta1**t)
    s_cor = new_s / (1 - beta2**t)
    new_var = var - alpha * v_cor / (np.sqrt(s_cor) + epsilon)
    return new_var, new_v, new_s
