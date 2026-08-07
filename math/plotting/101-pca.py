#!/usr/bin/env python3
"""
This module
"""
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

lib = np.load("pca.npz")
# data is a np.ndarray of shape (150, 4)
# 150 => the number of flowers
# 4 => petal length, petal width, sepal length, sepal width
data = lib["data"]
# labels is a np.ndarray of shape (150,)
# 0 => Iris Setosa
# 1 => Iris Versicolor
# 2 => Iris Virginica
labels = lib["labels"]

data_means = np.mean(data, axis=0)
norm_data = data - data_means
_, _, Vh = np.linalg.svd(norm_data)
pca_data = np.matmul(norm_data, Vh[:3].T)


x = pca_data[:, 0]
y = pca_data[:, 1]
z = pca_data[:, 2]
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.set_xlabel("U1")
ax.set_ylabel("U2")
ax.set_zlabel("U3")
ax.set_title("PCA of Iris Dataset")

ax.scatter(x, y, z, c=labels, cmap="plasma")

plt.savefig("101-pca.png")
plt.show()
