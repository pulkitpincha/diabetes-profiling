# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 16:07:01 2023

@author: stimp
"""

#importing libraries
import pandas as pd
import numpy as np
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster
import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_score
import seaborn as sns

#loading dataset
pima = pd.read_csv("C:/Users/stimp/OneDrive/Desktop/Flame/OPSM322/OPSM322_Homework-1/pima.csv")

#removing column
pima.drop(columns="diabetes", inplace=True)

#hierarchical clustering using ward
linkage_matrix = linkage(pima, method='ward')

#dendogram for finding optimal clusters using ward linkage
plt.figure(figsize=(10, 5))
dendrogram(linkage_matrix, truncate_mode='lastp', p=15) #p = number of clusters
plt.title('Dendrogram')
plt.xlabel('Data Points')
plt.ylabel('Distance')
plt.show()

#dendogram with optimal clusters
plt.figure(figsize=(10, 5))
dendrogram(linkage_matrix, truncate_mode='lastp', p=3) #p = number of clusters
plt.title('Dendrogram')
plt.xlabel('Data Points')
plt.ylabel('Distance')
plt.show()

#hierarchical clustering using single linkage
linkage_matrix = linkage(pima, method='single')

#dendrogram with clustering using single linkage
plt.figure(figsize=(10, 5))
dendrogram(linkage_matrix, truncate_mode='lastp', p=15) #p = number of clusters
plt.title('Dendrogram using single linkage')
plt.xlabel('Data Points')
plt.ylabel('Distance')
plt.show()

#hierarchical clustering using complete linkage
linkage_matrix = linkage(pima, method='complete')

#dendrogram with complete linkage
plt.figure(figsize=(10, 5))
dendrogram(linkage_matrix, truncate_mode='lastp', p=15) #p = number of clusters
plt.title('Dendrogram using complete linkage')
plt.xlabel('Data Points')
plt.ylabel('Distance')
plt.show()

#dendrogram with optimal clusters
plt.figure(figsize=(10, 5))
dendrogram(linkage_matrix, truncate_mode='lastp', p=3) #p = number of clusters
plt.title('Dendrogram')
plt.xlabel('Data Points')
plt.ylabel('Distance')
plt.show()

#silhouette score
num_clusters = 3
cluster_labels = fcluster(linkage_matrix, num_clusters, criterion='maxclust')
silhouette_avg = silhouette_score(pima, cluster_labels)
print(f"Silhouette Score: {silhouette_avg}")

#profiling the clusters using bar-plot
cluster_stats = pima.groupby(cluster_labels).mean()
plt.figure(figsize=(8, 5))
cluster_stats.plot(kind='bar', colormap='viridis', rot=0)
plt.xlabel('Cluster')
plt.ylabel('Mean Value')
plt.title('Bar-Plot')
leg = plt.legend(title='Feature', fontsize='xx-small', bbox_to_anchor=(0.5, -0.15), loc='upper center')

plt.show()

#profiling the clusters using scatter-plot
plt.figure(figsize=(10, 6))
for cluster in range(num_clusters):
    cluster_data = pima[cluster_labels == cluster]
    plt.scatter(cluster_data['pregnant'], cluster_data['age'], label=f'Cluster {cluster + 1}')

plt.xlabel('Pregnant')
plt.ylabel('Age')
plt.title('Cluster Profiling Using Scatterplot')
plt.legend()
plt.show()

#profiling the clusters box-plot
features = ['pregnant','glucose','pressure','triceps','insulin','mass','pedigree','age']
plt.figure(figsize=(15, 10))
for i, feature in enumerate(features, start=1):
    plt.subplot(3, 3, i)  # Adjust the subplot grid as needed
    sns.boxplot(x=cluster_labels, y=feature, data=pima)
    plt.xlabel('Cluster')
    plt.ylabel(feature)
    plt.title(f'Cluster Profiling Using Boxplot for {feature}')

plt.tight_layout()
plt.show()


