#!/usr/bin/env python3
"""
This module implements one function
def learning_rate_decay(alpha, decay_rate, decay_step)
"""
import tensorflow as tf


def learning_rate_decay(alpha, decay_rate, decay_step):
    """
    Function that creates a learning rate decay operation
    in tensorflow using inverse time decay.
    The decay occurs in a stepwise fashion.
    Args:
        alpha: is the original learning rate.
        decay_rate: is the weight used to determine the rate
            at which alpha will decay.
        decay_step: is the number of passes of gradient descent
            that should occur before alpha is decayed further.
    Returns:
        the learning rate decay operation.
    """
    return tf.keras.optimizers.schedules.InverseTimeDecay(
        alpha,
        decay_step,
        decay_rate,
        staircase=True,
        name='InverseTimeDecay'
    )
