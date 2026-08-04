#!/usr/bin/env python3
"""
This module implement one function line()
"""
import numpy as np
import matplotlib.pyplot as plt


def line():
    """
    This plot y as a line graph
    """
    y = np.arange(0, 11) ** 3
    plt.figure(figsize=(6.4, 4.8))

    x = np.arange(0, 11)
    plt.plot(x, y, c='r')
    plt.savefig("graph.png")
