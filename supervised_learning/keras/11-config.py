#!/usr/bin/env python3
"""
This module implements two functions that save and
load a model's configuration in JSON format.
"""
import tensorflow.keras as K


def save_config(network, filename):
    """
    Function that saves a model's configuration in JSON format
    Args:
        network: the model whose configuration should be saved.
        filename: the path of the file that the configuration
            should be saved to.
    Returns: None
    """
    with open(filename, 'w') as file:
        file.write(network.to_json())
    return None


def load_config(filename):
    """
    Function that loads a model with a specific configuration.
    Args:
        filename: the path of the file containing the model's
            configuration in JSON format.
    Returns: the loaded model.
    """
    with open(filename, 'r') as file:
        model = K.models.model_from_json(file.read())
    return model
