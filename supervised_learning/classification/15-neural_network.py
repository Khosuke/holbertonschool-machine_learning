#!/usr/bin/env python3
"""
This module defines a single class NeuralNetwork
"""
import numpy as np
import matplotlib.pyplot as plt


class NeuralNetwork:
    """
    This class defines a neural network with one hidden
    layer performing binary classification.
    Attributes:
        W1: The weights vector for the hidden layer.
        b1: The bias for the hidden layer.
        A1: The activated output for the hidden layer.
        W2: The weights vector for the output neuron.
        b2: The bias for the output neuron.
        A2: The activated output for the output neuron (prediction).
    """
    def __init__(self, nx, nodes):
        """
        Class constructor
        Args:
            nx: number of input features
            nodes: number of nodes found in the hidden layer
        """
        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        if not isinstance(nodes, int):
            raise TypeError("nodes must be an integer")
        if nodes < 1:
            raise ValueError("nodes must be a positive integer")
        self.__W1 = np.random.randn(nodes, nx)
        self.__b1 = np.zeros((nodes, 1))
        self.__A1 = 0
        self.__W2 = np.random.randn(1, nodes)
        self.__b2 = 0
        self.__A2 = 0

    @property
    def W1(self):
        return self.__W1

    @property
    def b1(self):
        return self.__b1

    @property
    def A1(self):
        return self.__A1

    @property
    def W2(self):
        return self.__W2

    @property
    def b2(self):
        return self.__b2

    @property
    def A2(self):
        return self.__A2

    def forward_prop(self, X):
        """
        Function that calculates the forward propagation of the neural network.
        Args:
            X: a numpy.ndarray with shape (nx, m)
                where nx is the number of input features to the neuron
                and m is the number of examples.
        """
        self.__A1 = 1 / (1 + np.exp(-(np.dot(self.W1, X) + self.b1)))
        self.__A2 = 1 / (1 + np.exp(-(np.dot(self.W2, self.A1) + self.b2)))

        return self.__A1, self.__A2

    def cost(self, Y, A):
        """
        Calculates the cost of the model using logistic regression
        Args:
            Y: a numpy.ndarray with shape (1, m) that contains
                the correct labels for the input data.
            A: a numpy.ndarray with shape (1, m) containing the activated
                output of the neuron for each example.
        """
        loss = -(Y * np.log(A) + (1 - Y) * np.log(1.0000001 - A))
        return ((1/Y.shape[1]) * np.sum(loss))

    def evaluate(self, X, Y):
        """
        Evaluates the neural network's predictions
        Args:
            X: a numpy.ndarray with shape (nx, m) that contains
                the input data.
            Y: a numpy.ndarray with shape (1, m) that contains
                the correct labels for the input data.
        """
        A1, A2 = self.forward_prop(X)
        cost = self.cost(Y, A2)
        pred = np.where(A2 >= 0.5, 1, 0)

        return pred, cost

    def gradient_descent(self, X, Y, A1, A2, alpha=0.05):
        """
        Calculates one pass of gradient descent on the neural network
        Args:
            X: a numpy.ndarray with shape (nx, m)
                that contains the input data,
                where nx is the number of input features to the neuron
                and m is the number of examples.
            Y: a numpy.ndarray with shape (1, m)
                that contains the correct labels for the input data.
            A1: the output of the hidden layer.
            A2: the predicted output.
            alpha: the learning rate.
        """
        m = Y.shape[1]

        pred_dif2 = A2 - Y

        weight_gradient2 = (1 / m) * np.matmul(pred_dif2, A1.T)
        bias_gradient2 = (1 / m) * np.sum(pred_dif2, axis=1, keepdims=True)

        pred_dif1 = np.matmul(self.W2.T, pred_dif2) * (A1 * (1 - A1))

        weight_gradient1 = (1 / m) * np.matmul(pred_dif1, X.T)
        bias_gradient1 = (1 / m) * np.sum(pred_dif1, axis=1, keepdims=True)

        self.__W1 = self.W1 - alpha * weight_gradient1
        self.__b1 = self.b1 - alpha * bias_gradient1
        self.__W2 = self.W2 - alpha * weight_gradient2
        self.__b2 = self.b2 - alpha * bias_gradient2

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

        costs = []
        iters = []

        for i in range(iterations):
            A1, A2 = self.forward_prop(X)
            cost = self.cost(Y, A2)

            if i % step == 0 or i == iterations:
                costs.append(cost)
                iters.append(i)
                if verbose:
                    print("Cost after {} iterations: {}".format(i, cost))

            if i < iterations:
                self.gradient_descent(X, Y, A1, A2, alpha)

        if graph:
            plt.plot(iters, costs, 'b-')
            plt.xlabel('iteration')
            plt.ylabel('cost')
            plt.title('Training Cost')
            plt.show()

        return self.evaluate(X, Y)
