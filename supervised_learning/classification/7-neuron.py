#!/usr/bin/env python3
"""
This module defines a single class Neuron
"""
import numpy as np
import matplotlib.pyplot as plt


class Neuron:
    """
    defines a single neuron performing binary classification
    """
    def __init__(self, nx):
        """
        Class constructor
        Args:
            nx: the number of input features to the neuron
        Attributes:
            __W: The weights vector for the neuron.
            __b: The bias for the neuron.
            __A: The activated output of the neuron (prediction).
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

    def cost(self, Y, A):
        """
        Calculates the cost of the model using logistic regression
        Args:
            Y: a numpy.ndarray with shape (1, m)
                that contains the correct labels for the input data.
            A: a numpy.ndarray with shape (1, m)
                containing the activated output of the neuron
                for each example.
        """
        loss = -(Y * np.log(A) + (1 - Y) * np.log(1.0000001 - A))
        return ((1/Y.shape[1]) * np.sum(loss))

    def evaluate(self, X, Y):
        """
        Evaluates the neuron's predictions
        Args:
            X: a numpy.ndarray with shape (nx, m)
                that contains the input data,
                where nx is the number of input features to the neuron
                and m is the number of examples.
            Y: a numpy.ndarray with shape (1, m)
                that contains the correct labels for the input data.
        """
        A = self.forward_prop(X)
        cost = self.cost(Y, A)
        pred = np.where(A >= 0.5, 1, 0)

        return pred, cost

    def gradient_descent(self, X, Y, A, alpha=0.05):
        """
        Calculates one pass of gradient descent on the neuron
        Args:
            X: a numpy.ndarray with shape (nx, m)
                that contains the input data,
                where nx is the number of input features to the neuron
                and m is the number of examples.
            Y: a numpy.ndarray with shape (1, m)
                that contains the correct labels for the input data.
            A: a numpy.ndarray with shape (1, m)
                containing the activated output of the neuron for each example.
            alpha: the learning rate.
        """
        m = Y.shape[1]

        pred_dif = A - Y
        weight_gradient = (1 / m) * np.matmul(pred_dif, X.T)
        bias_gradient = (1 / m) * np.sum(pred_dif)

        self.__W = self.W - alpha * weight_gradient
        self.__b = self.b - alpha * bias_gradient

    def train(self, X, Y, iterations=5000, alpha=0.05,
              verbose=True, graph=True, step=100):
        """
        Trains the neuron
        Args:
            X: a numpy.ndarray with shape (nx, m)
                that contains the input data,
                where nx is the number of input features to the neuron
                and m is the number of examples.
            Y: a numpy.ndarray with shape (1, m)
                that contains the correct labels for the input data.
            iterations: number of iterations to train over.
            alpha: the learning rate.
            verbose: defines whether or not to print information
                about the training.
            graph: defines whether or not to graph information
                about the training.
            step: used to print or plot data every step iterations.
        """
        if not isinstance(iterations, int):
            raise TypeError("iterations must be an integer")
        if iterations < 0:
            raise ValueError("iterations must be a positive integer")
        if not isinstance(alpha, float):
            raise TypeError("alpha must be a float")
        if alpha < 0:
            raise ValueError("alpha must be positive")
        if verbose or graph:
            if not isinstance(step, int):
                raise TypeError("step must be an integer")
            if step < 1 or step > iterations:
                raise ValueError("step must be positive and <= iterations")

        costs = []
        iters = []

        for i in range(iterations + 1):
            A = self.forward_prop(X)
            cost = self.cost(Y, A)

            if i % step == 0 or i == iterations:
                costs.append(cost)
                iters.append(i)
                if verbose:
                    print("Cost after {} iterations: {}".format(i, cost))

            if i < iterations:
                self.gradient_descent(X, Y, A, alpha)

        if graph:
            plt.plot(iters, costs, 'b-')
            plt.xlabel('iteration')
            plt.ylabel('cost')
            plt.title('Training Cost')
            plt.show()

        return self.evaluate(X, Y)
