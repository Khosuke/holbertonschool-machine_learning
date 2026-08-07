#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

def gradient():

    np.random.seed(5)

    x = np.random.randn(2000) * 10
    y = np.random.randn(2000) * 10
    z = np.random.rand(2000) + 40 - np.sqrt(np.square(x) + np.square(y))
    plt.figure(figsize=(6.4, 4.8))

    plt.xlim(-40, 40)
    plt.ylim(-40, 40)
    plt.xticks(range(-30, 31, 10))
    plt.yticks(range(-30, 31, 10))
    plt.xlabel("x coordinate (m)")
    plt.ylabel("y coordinate (m)")
    plt.title("Mountain Elevation")
    plt.scatter(x, y, c=z)
    plt.colorbar(label="elevation (m)")

    plt.savefig("100-graph.png")
