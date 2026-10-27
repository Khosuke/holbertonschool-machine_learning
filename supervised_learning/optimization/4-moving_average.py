#!/usr/bin/env python3
"""
This module implements one function
def moving_average(data, beta)
"""


def moving_average(data, beta):
    """
    Function that calculates the weighted moving average of a data set
    using bias correction.
    Args:
        data: the list of data to calculate the moving average of.
        beta: the weight used for the moving average.
    Returns:
        a list containing the moving averages of data.
    """
    v = 0
    averages = []
    for i, x in enumerate(data, 1):
        v = beta * v + (1 - beta) * x
        averages.append(v / (1 - beta**i))

    return averages
