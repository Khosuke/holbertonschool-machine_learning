#!/usr/bin/env python3
"""
This module implements two function to save and load models.
"""
import tensorflow.keras as K


def save_model(network, filename):
    """
    This function saves an entire model.
    Args:
        network: The model to save.
        filename: The path of the file that the model
            should be saved to.
    Returns: None
    """
    network.save(filename)
    return None


def load_model(filename):
    """
    This function loads an entire model.
    Arg:
        filename: The path of the file that the model
            should be loaded from.
    Return: The loaded model.
    """
    model = K.models.load_model(filename)
    return model
