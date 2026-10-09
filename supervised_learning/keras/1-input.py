#!/usr/bin/env python3
"""
This module implements one function def build_model()
"""
import tensorflow.keras as K


def build_model(nx, layers, activations, lambtha, keep_prob):
    """
    This function builds a neural network.
    Args:
        nx: the number of input features to the network.
        layers: list containing the number of nodes
            in each layer of the network.
        activations: list containing the activation functions used
            for each layer of the network.
        lambtha: the L2 regularization parameter.
        keep_prob: the probability that a node will be kept for dropout.
    """
    inputs = K.Input(shape=(nx,))
    output = inputs
    L2 = K.regularizers.L2(lambtha)
    for i in range(len(layers)):
        output = K.layers.Dense(layers[i], activation=activations[i],
                                kernel_regularizer=L2)(output)
        if i < len(layers) - 1:
            output = K.layers.Dropout(1 - keep_prob)(output)
    model = K.Model(inputs=inputs, outputs=output)
    return model
