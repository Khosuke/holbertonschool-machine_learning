# Project : Optimization


## Task 0. Normalization Constants

Write the function `def normalization_constants(X):` that calculates the normalization (standardization) constants of a matrix:

- `X` is the `numpy.ndarray` of shape `(m, nx)` to normalize
    - `m` is the number of data points
    - `nx` is the number of features
- Returns: the mean and standard deviation of each feature, respectively

File: [0-norm_constants.py](0-norm_constants.py)

## Task 1. Normalize

Write the function` def normalize(X, m, s):` that normalizes (standardizes) a matrix:

- `X` is the `numpy.ndarray` of shape `(d, nx)` to normalize
    - d is the number of data points
    - nx is the number of features
- `m` is a `numpy.ndarray` of shape `(nx,)` that contains the mean of all features of `X`
- `s` is a `numpy.ndarray` of shape `(nx,)` that contains the standard deviation of all features of `X`
- Returns: The normalized `X` matrix

File: [1-normalize.py](1-normalize.py)

## Task 2. Shuffle Data

Write the function `def shuffle_data(X, Y):` that shuffles the data points in two matrices the same way:

- `X` is the first `numpy.ndarray` of shape `(m, nx)` to shuffle
    - `m` is the number of data points
    - `nx` is the number of features in `X`
- `Y` is the second `numpy.ndarray` of shape `(m, ny)` to shuffle
    - `m` is the same number of data points as in `X`
    - `ny` is the number of features in `Y`
- Returns: the shuffled `X` and `Y` matrices

File: [2-shuffle_data.py](2-shuffle_data.py)

## Task 3. Mini-Batch

Write a function `def create_mini_batches(X, Y, batch_size):` that creates mini-batches to be used for training a neural network using mini-batch gradient descent:

- `X` is a `numpy.ndarray` of shape `(m, nx)` representing input data
    - `m` is the number of data points
    - `nx` is the number of features in `X`
- `Y` is a `numpy.ndarray` of shape `(m, ny)` representing the labels
    - `m` is the same number of data points as in `X`
    - `ny` is the number of classes for classification tasks.
- `batch_size` is the number of data points in a batch
- Returns: list of mini-batches containing tuples `(X_batch, Y_batch)`
- Your function should allow for a smaller final batch (i.e. use the entire dataset)
- You should use `shuffle_data = __import__('2-shuffle_data').shuffle_data`

File: [3-mini_batch.py](3-mini_batch.py)

## Task 4. Moving Average

Write the function `def moving_average(data, beta):` that calculates the weighted moving average of a data set:

- `data` is the list of data to calculate the moving average of
- `beta` is the weight used for the moving average
- Your moving average calculation should use bias correction
- Returns: a list containing the moving averages of data

File: [4-moving_average.py](4-moving_average.py)

## Task 5. Momentum

Write the function `def update_variables_momentum(alpha, beta1, var, grad, v):` that updates a variable using the gradient descent with momentum optimization algorithm:

- `alpha` is the learning rate
- `beta1` is the momentum weight
- `var` is a `numpy.ndarray` containing the variable to be updated
- `grad` is a `numpy.ndarray` containing the gradient of `var`
- `v` is the previous first moment of `var`
- Returns: the updated variable and the new moment, respectively

File: [5-momentum.py](5-momentum.py)

## Task 7. RMSProp

Write the function `def update_variables_RMSProp(alpha, beta2, epsilon, var, grad, s):` that updates a variable using the RMSProp optimization algorithm:

- `alpha` is the learning rate
- `beta2` is the RMSProp weight
- `epsilon` is a small number to avoid division by zero
- `var` is a `numpy.ndarray` containing the variable to be updated
- `grad` is a `numpy.ndarray` containing the gradient of `var`
- `s` is the previous second moment of `var`
- Returns: the updated variable and the new moment, respectively

File: [7-RMSProp.py](7-RMSProp.py)

## Task 9. Adam

Write the function `def update_variables_Adam(alpha, beta1, beta2, epsilon, var, grad, v, s, t):` that updates a variable in place using the Adam optimization algorithm:

- `alpha` is the learning rate
- `beta1` is the weight used for the first moment
- `beta2` is the weight used for the second moment
- `epsilon` is a small number to avoid division by zero
- `var` is a `numpy.ndarray` containing the variable to be updated
- `grad` is a `numpy.ndarray` containing the gradient of `var`
- `v` is the previous first moment of `var`
- `s` is the previous second moment of `var`
- `t` is the time step used for bias correction
- Returns: the updated variable, the new first moment, and the new second moment, respectively

File: [9-Adam.py](9-Adam.py)

## Task 11. Learning Rate Decay

Write the function `def learning_rate_decay(alpha, decay_rate, global_step, decay_step):` that updates the learning rate using inverse time decay in numpy:

- `alpha` is the original learning rate
- `decay_rate` is the weight used to determine the rate at which `alpha` will decay
- `global_step` is the number of passes of gradient descent that have elapsed
- `decay_step` is the number of passes of gradient descent that should occur before `alpha` is decayed further
- the learning rate decay should occur in a stepwise fashion
- Returns: the updated value for `alpha`

File: [11-learning_rate_decay.py](11-learning_rate_decay.py)

## Task 12. Learning Rate Decay Upgraded

Write the function d`ef learning_rate_decay(alpha, decay_rate, decay_step):` that creates a learning rate decay operation in `tensorflow` using inverse time decay:

- `alpha` is the original learning rate
- `decay_rate` is the weight used to determine the rate at which `alpha` will decay
- `decay_step` is the number of passes of gradient descent that should occur before `alpha` is decayed further
- the learning rate decay should occur in a stepwise fashion
- Returns: the learning rate decay operation

File: [12-learning_rate_decay.py](12-learning_rate_decay.py)
