# Project : Regularization

## Task 0. L2 Regularization Cost

Write a function `def l2_reg_cost(cost, lambtha, weights, L, m):` that calculates the cost of a neural network with L2 regularization:

- `cost` is the cost of the network without L2 regularization
- `lambtha` is the regularization parameter
- `weights` is a dictionary of the weights and biases (`numpy.ndarrays`) of the neural network
- `L` is the number of layers in the neural network
- `m` is the number of data points used
- Returns: the cost of the network accounting for L2 regularization

File: [0-l2_reg_cost.py](0-l2_reg_cost.py)

## Task 1. Gradient Descent with L2 Regularization

Write a function def l2_reg_gradient_descent(Y, weights, cache, alpha, lambtha, L): that updates the weights and biases of a neural network using gradient descent with L2 regularization:

- `Y` is a one-hot numpy.ndarray of shape `(classes, m)` that contains the correct labels for the data
    - `classes` is the number of classes
    - `m` is the number of data points
- `weights` is a dictionary of the weights and biases of the neural network
- `cache` is a dictionary of the outputs of each layer of the neural network
- `alpha` is the learning rate
- `lambtha` is the L2 regularization parameter
- `L` is the number of layers of the network
- The neural network uses `tanh` activations on each layer except the last, which uses a `softmax` activation
- The weights and biases of the network should be updated in place

File: [1-l2_reg_gradient_descent.py](1-l2_reg_gradient_descent.py)

## Task 4. Forward Propagation with Dropout

Write a function `def dropout_forward_prop(X, weights, L, keep_prob):` that conducts forward propagation using Dropout:

- `X` is a `numpy.ndarray` of shape `(nx, m)` containing the input data for the network
    - `nx` is the number of input features
    - `m` is the number of data points
- `weights` is a dictionary of the weights and biases of the neural network
- `L` the number of layers in the network
- `keep_prob` is the probability that a node will be kept
- All layers except the last should use the `tanh` activation function
- The last layer should use the `softmax` activation function
- Returns: a dictionary containing the outputs of each layer and the dropout mask used on each layer (see example for format)

File: [4-dropout_forward_prop.py](4-dropout_forward_prop.py)

## Task 7. Early Stopping

Write the function `def early_stopping(cost, opt_cost, threshold, patience, count):` that determines if you should stop gradient descent early:

- Early stopping should occur when the validation cost of the network has not decreased relative to the optimal validation cost by more than the threshold over a specific patience count
- `cost` is the current validation cost of the neural network
- `opt_cost` is the lowest recorded validation cost of the neural network
- `threshold` is the threshold used for early stopping
- `patience` is the patience count used for early stopping
- `count` is the count of how long the threshold has not been met
- Returns: a boolean of whether the network should be stopped early, followed by the updated count

File: [7-early_stopping.py](7-early_stopping.py)
