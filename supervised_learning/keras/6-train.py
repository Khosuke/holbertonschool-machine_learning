#!/usr/bin/env python3
"""
This module implement one function def train_model()
"""
import tensorflow.keras as K


def train_model(network, data, labels, batch_size, epochs,
                validation_data=None, early_stopping=False,
                patience=0, verbose=True, shuffle=False):
    """
    Function that trains a model using mini-batch gradient descent
        and also analyze validaiton data.
    Args:
        network: the model to train.
        data: numpy.ndarray of shape (m, nx) containing
            the input data.
        labels: one-hot numpy.ndarray of shape (m, classes)
            containing the labels of data.
        batch_size: the size of the batch used for mini-batch
            gradient descent.
        epochs: the number of passes through data for mini-batch
            gradient descent.
        verbose: boolean that determines if output should be printed
            during training.
        validation_data: the data to validate the model with, if not None.
        early_stopping: a boolean that indicates whether
            early stopping should be used.
        patience: the patience used for early stopping.
        shuffle: boolean that determines whether to shuffle the batches
            every epoch. Default to False.

    Returns:
        the History object generated after training the model.
    """
    if early_stopping:
        callbacks = K.callbacks.EarlyStopping(monitor='val_loss',
                                              patience=patience, mode='min')
    else:
        callbacks = None

    history = network.fit(
            x=data,
            y=labels,
            batch_size=batch_size,
            epochs=epochs,
            verbose=verbose,
            validation_data=validation_data,
            callbacks=callbacks,
            shuffle=shuffle
        )
    return history
