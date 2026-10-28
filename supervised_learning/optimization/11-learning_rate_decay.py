#!/usr/bin/env python3
"""
This module implements one function
def learning_rate_decay(alpha, decay_rate, global_step, decay_step)
"""
import numpy as np


def learning_rate_decay(alpha, decay_rate, global_step, decay_step):
    """
    Function that updates the learning rate using inverse time decay
    in numpy. The decay occurs in a stepwise fashion.
    Args:
        alpha: is the original learning rate.
        decay_rate: is the weight used to determine the rate
            at which alpha will decay.
        global_step: is the number of passes of gradient descent
            that have elapsed.
        decay_step: is the number of passes of gradient descent
            that should occur before alpha is decayed further.
    Returns:
        the updated value for alpha.
    """
    return alpha / (1 + decay_rate * np.floor(global_step / decay_step))
