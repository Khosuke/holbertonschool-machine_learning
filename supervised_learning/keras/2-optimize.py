#!/usr/bin/env python3
"""
This module implements one function def optimize_model()
"""
import tensorflow.keras as K


def optimize_model(network, alpha, beta1, beta2):
    """
    Function that sets up Adam optimization for a keras model
    with categorical crossentropy loss and accuracy metrics.
    Args:
        network: the model to optimize.
        alpha: the learning rate.
        beta1: the first Adam optimization parameter.
        beta2: the second Adam optimization parameter.
    """
    opt = K.optimizers.Adam(alpha, beta1, beta2)
    network.compile(loss='categorical_crossentropy',
                    optimizer=opt, metrics=["accuracy"])
