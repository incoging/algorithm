#!/usr/bin/python
# -*- coding: UTF-8 -*-
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.patches import Circle
from sklearn.neighbors import KDTree

np.random.seed(0)
points = np.random.random((100, 2))
print(points)
tree = KDTree(points)
point = points[0]
# kNN
dists, indices = tree.query([point], k=3)  #求距离point点最近的3个点，返回响应的距离和这3个点的索引。
print("dists=", dists)
print("indices=", indices)
# print(dists, indices)
# query radius
indices = tree.query_radius([point], r=0.3) #求取距离point为r的点的索引。
print("indices=", indices)
fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')
ax.add_patch(Circle(point, 0.2, color='r', fill=False))
X, Y = [p[0] for p in points], [p[1] for p in points]
plt.scatter(X, Y)
plt.scatter([point[0]], [point[1]], c='r')
plt.show()
