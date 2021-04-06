# TUTORIAL DE
# https://towardsdatascience.com/machine-learning-algorithms-part-9-k-means-example-in-python-f2ad05ed5203

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

X, y = make_blobs(
    n_samples=300, 
    centers=4, 
    cluster_std=0.60, 
    random_state=0
)

plt.scatter(X[:,0], X[:,1], c='blue')
plt.show()


# explicacion KMeans: https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html
wcss = []
for i in range(1, 11):
    kmeans = KMeans(
        n_clusters=i, 
        init='k-means++', 
        max_iter=300, 
        n_init=10, 
        random_state=0
    )
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
plt.plot(range(1, 11), wcss)
plt.title('Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()


kmeans = KMeans(
    n_clusters=4, 
    init='k-means++', 
    max_iter=300, 
    n_init=10, 
    random_state=0
)
pred_y = kmeans.fit_predict(X)
print("KMEANS")
print(pred_y)
for i in range(0,pred_y.size):
    if pred_y[i] == 0:
        plt.scatter(X[i,0], X[i,1], c='pink')
    if pred_y[i] == 1:
        plt.scatter(X[i,0], X[i,1], c='blue')
    if pred_y[i] == 2:
        plt.scatter(X[i,0], X[i,1], c='green')
    if pred_y[i] == 3:
        plt.scatter(X[i,0], X[i,1], c='yellow')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=150, c='red')
plt.show()