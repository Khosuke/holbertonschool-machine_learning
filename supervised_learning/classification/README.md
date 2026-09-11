# Project : Classification Using Neural Networks


At the end of this project, we should be able to build our own binary image classifier from scratch using `numpy`


## Task 0. Neuron

Write a class `Neuron` that defines a single neuron performing binary classification:

- class constructor: `def __init__(self, nx):`
    - `nx` is the number of input features to the neuron
        - If `nx` is not an integer, raise a `TypeError` with the exception: `nx must be an integer`
        - If `nx` is less than 1, raise a `ValueError` with the exception: `nx must be a positive integer`
    - All exceptions should be raised in the order listed above
- Public instance attributes:
    - `W`: The weights vector for the neuron. Upon instantiation, it should be initialized using a random normal distribution.
    - `b`: The bias for the neuron. Upon instantiation, it should be initialized to 0.
    - `A`: The activated output of the neuron (prediction). Upon instantiation, it should be initialized to 0.

File: [0-neuron.py](0-neuron.py)

## Task 1. Privatize Neuron

Write a class `Neuron` that defines a single neuron performing binary classification (Based on [0-neuron.py](0-neuron.py)):

- class constructor: `def __init__(self, nx):`
    - `nx` is the number of input features to the neuron
        - If `nx` is not an integer, raise a `TypeError` with the exception: `nx must be an integer`
        - If `nx` is less than 1, raise a `ValueError` with the exception: `nx must be a positive`
    - All exceptions should be raised in the order listed above
- Public instance attributes:
    - `__W`: The weights vector for the neuron. Upon instantiation, it should be initialized using a random normal distribution.
    - `__b`: The bias for the neuron. Upon instantiation, it should be initialized to 0.
    - `__A`: The activated output of the neuron (prediction). Upon instantiation, it should be initialized to 0.
    - Each private attribute should have a corresponding getter function (no setter function).

File: [1-neuron.py](1-neuron.py)

## Task 2. Neuron Forward Propagation

Write a class `Neuron` that defines a single neuron performing binary classification (Based on [1-neuron.py](1-neuron.py)):

- Add the public method `def forward_prop(self, X)`:
    - Calculates the forward propagation of the neuron
    - `X` is a `numpy.ndarray` with shape (`nx`, `m`) that contains the input data
        - `nx` is the number of input features to the neuron
        - `m` is the number of examples
    - Updates the private attribute `__A`
    - The neuron should use a sigmoid activation function
    - Returns the private attribute `__A`

File: [2-neuron.py](2-neuron.py)

## Task 3. Neuron Cost

Write a class `Neuron` that defines a single neuron performing binary classification (Based on [2-neuron.py](2-neuron.py)):

- Add the public method def cost(self, Y, A):
    - Calculates the cost of the model using logistic regression
    - `Y` is a `numpy.ndarray` with shape (1, `m`) that contains the correct labels for the input data
    - `A` is a `numpy.ndarray` with shape (1, `m`) containing the activated output of the neuron for each example
    - To avoid division by zero errors, please use `1.0000001 - A` instead of `1 - A`
    - Returns the cost

File: [3-neuron.py](3-neuron.py)

## Task 4. Evaluate Neuron

Write a class `Neuron` that defines a single neuron performing binary classification (Based on [3-neuron.py](3-neuron.py)):

- Add the public method `def evaluate(self, X, Y):`
    - Evaluates the neuron's predictions
    - `X` is a `numpy.ndarray` with shape (`nx`, `m`) that contains the input data
        - nx is the number of input features to the neuron
        - m is the number of examples
    - `Y` is a `numpy.ndarray` with shape (1, `m`) that contains the correct labels for the input data
    - Returns the neuron's prediction and the cost of the network, respectively
        - The prediction should be a `numpy.ndarray` with shape (1, `m`) containing the predicted labels for each example
        - The label values should be 1 if the output of the network is >= 0.5 and 0 otherwise

File: [4-neuron.py](4-neuron.py)

## Task 5. Neuron Gradient Descent

Write a class `Neuron` that defines a single neuron performing binary classification (Based on [4-neuron.py](4-neuron.py)):

- Add the public method `def gradient_descent(self, X, Y, A, alpha=0.05):`
    - Calculates one pass of gradient descent on the neuron
    - `X` is a `numpy.ndarray` with shape (`nx`, `m`) that contains the input data
        - nx is the number of input features to the neuron
        - m is the number of examples
    - `Y` is a `numpy.ndarray` with shape (1, `m`) that contains the correct labels for the input data
    - `A` is a `numpy.ndarray` with shape (1, `m`) containing the activated output of the neuron for each example
    - `alpha` is the learning rate
    - Updates the private attributes `__W` and `__b`


File: [5-neuron.py](5-neuron.py)

## Task 6. Train Neuron

Write a class `Neuron` that defines a single neuron performing binary classification (Based on [5-neuron.py](5-neuron.py)):

- Add the public method `def train(self, X, Y, iterations=5000, alpha=0.05):`
    - Trains the neuron
    - `X` is a `numpy.ndarray` with shape (`nx`, `m`) that contains the input data
        - `nx` is the number of input features to the neuron
        - `m` is the number of examples
    - `Y` is a `numpy.ndarray` with shape (1, `m`) that contains the correct labels for the input data
    - `iterations` is the number of iterations to train over
        - if `iterations` is not an integer, raise a `TypeError` with the exception `iterations must be an integer`
        - if `iterations` is not positive, raise a `ValueError` with the exception `iterations must be a positive integer`
    - `alpha` is the learning rate
        - if `alpha` is not a float, raise a `TypeError` with the exception `alpha must be a float`
        - if `alpha` is not positive, raise a `ValueError` with the exception `alpha must be positive`
    - All exceptions should be raised in the order listed above
    - Updates the private attributes `__W`, `__b`, and `__A`
    - You are allowed to use one loop
    - Returns the evaluation of the training data after `iterations` of training have occurred

File: [6-neuron.py](6-neuron.py)


## Task 7. Upgrade Train Neuron

Write a class `Neuron` that defines a single neuron performing binary classification (Based on 6-neuron.py):

- Update the public method train to `def train(self, X, Y, iterations=5000, alpha=0.05, verbose=True, graph=True, step=100):`
    - Trains the neuron by updating the private attributes `__W`, `__b`, and `__A`
    - `X` is a numpy.ndarray with shape (`nx`, `m`) that contains the input data
        - `nx` is the number of input features to the neuron
        - `m` is the number of examples
    - `Y` is a numpy.ndarray with shape (1, `m`) that contains the correct labels for the input data
    - `iterations` is the number of iterations to train over
        - if `iterations` is not an integer, raise a `TypeError` with the exception `iterations must be an integer`
        - if `iterations` is not positive, raise a `ValueError` with the exception `iterations must be a positive integer`
    - `alpha` is the learning rate
        - if `alpha` is not a float, raise a `TypeError` with the exception `alpha must be a float`
        - if `alpha` is not positive, raise a `ValueError` with the exception `alpha must be positive`
    - `verbose` is a boolean that defines whether or not to print information about the training. If `True`, print `Cost after {iteration} iterations: {cost}` every `step` iterations:
        - Include data from the 0th and last iteration
    - `graph` is a boolean that defines whether or not to graph information about the training once the training has completed. If `True`:
        - Plot the training data every `step` iterations as a blue line
        - Label the x-axis as `iteration`
        - Label the y-axis as `cost`
        - Title the plot `Training Cost`
        - Include data from the 0th and last iteration
    - Only if either `verbose` or `graph` are `True`:
        - if `step` is not an integer, raise a `TypeError` with the exception `step must be an integer`
        - if `step` is not positive or is greater than `iterations`, raise a `ValueError` with the exception `step must be positive and <= iterations`
    - All exceptions should be raised in the order listed above
    - The 0th iteration should represent the state of the neuron before any training has occurred
    - You are allowed to use one loop
    - You can use `import matplotlib.pyplot as plt`
    - Returns: the evaluation of the training data after `iterations` of training have occurred

File: [7-neuron.py](7-neuron.py)

## Task 

## Task 


## Task 

## Task 


## Task 

## Task 


## Task 

## Task 

