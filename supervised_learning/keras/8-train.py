#!/usr/bin/env python3
"""
This module implement one function def train_model()
"""
import tensorflow.keras as K


def train_model(network, data, labels, batch_size, epochs,
                validation_data=None, early_stopping=False,
                patience=0, learning_rate_decay=False, alpha=0.1,
                decay_rate=1, save_best=False, filepath=None,
                verbose=True, shuffle=False):
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
        learning_rate_decay: boolean that indicates whether learning
            rate decay should be used.
        alpha: the initial learning rate.
        decay_rate: the decay rate.
        save_best: boolean indicating whether to save the model after
            each epoch if it is the best.
        filepath: the file path where the model should be saved.
    Returns:
        the History object generated after training the model.
    """
    callbacks = []

    def scheduler(epoch):
        """
        Computes the learning rate for an epoch using inverse time decay.
        Args:
            epoch: the index of the current epoch, starting at 0.
        Returns:
            the learning rate for this epoch.
        """
        return alpha / (1 + decay_rate * epoch)

    if validation_data is not None and early_stopping:
        callbacks.append(
            K.callbacks.EarlyStopping(
                monitor='val_loss', patience=patience, mode='min')
                )
    if validation_data is not None and learning_rate_decay:
        callbacks.append(
            K.callbacks.LearningRateScheduler(
                schedule=scheduler, verbose=1)
                )
    if validation_data is not None and save_best:
        callbacks.append(
            K.callbacks.ModelCheckpoint(
                filepath=filepath, monitor="val_loss", save_best_only=True)
                )

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
