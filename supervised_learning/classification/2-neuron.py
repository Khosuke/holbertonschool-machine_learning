#!/usr/bin/env python3
"""
This module defines a single class Neuron
"""
import numpy as np


class Neuron:
    """
    defines a single neuron performing binary classification
    """
    def __init__(self, nx):
        """
        Class constructor
        Args:
            nx: the number of input features to the neuron
        """
        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        self.__W = np.random.randn(1, nx)
        self.__b = 0
        self.__A = 0

    @property
    def W(self):
        return self.__W

    @property
    def b(self):
        return self.__b

    @property
    def A(self):
        return self.__A

    def forward_prop(self, X):
        """
        Calculates the forward propagation of the neuron
        Args:
            X: a numpy.ndarray with shape (nx, m)
            that contains the input data
            where nx is the number of input features to the neuron
            and m is the number of examples
        """
        self.__A = 1 / (1 + np.exp(-(np.dot(self.W, X) + self.b)))
        return self.__A
