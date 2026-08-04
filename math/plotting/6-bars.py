#!/usr/bin/env python3
"""
This module implements one function bars()
"""
import numpy as np
import matplotlib.pyplot as plt


def bars():
    """
    Function to plot a stacked bar graph
    """
    np.random.seed(5)
    fruit = np.random.randint(0, 20, (4,3))
    plt.figure(figsize=(6.4, 4.8))

    names = ['Farrah', 'Fred', 'Felicia']
    colors = ['red', 'yellow', '#ff8000', '#ffe5b4']
    fruits = ['apples', 'bananas', 'oranges', 'peaches']

    bottom = [0, 0, 0]
    for i in range(4):
        plt.bar(names, fruit[i], width=0.5, bottom=bottom,
                color=colors[i], label=fruits[i])
        bottom += fruit[i]

    plt.ylabel('Quantity of Fruit')
    plt.ylim(0, 80)
    plt.yticks(np.arange(0, 81, 10))
    plt.title('Number of Fruit per Person')
    plt.legend()

    plt.savefig("6-graph.png")

