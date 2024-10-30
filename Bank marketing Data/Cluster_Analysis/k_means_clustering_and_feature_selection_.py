# -*- coding: utf-8 -*-
"""K-Means Clustering and Feature Selection .ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1QHkkpjU-mKGcTbdEP2xfCxfiH6EhuZgo

##Importing Necessary Libraries
Brings in all required libraries for data manipulation, clustering, and visualization.
"""

# Importing necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

"""##Load Dataset and Check for Missing Values
2)Ensures data integrity by checking for any missing values.

1)Loads and provides an initial look at the dataset.

"""

# Load the dataset
data = pd.read_csv('bank-direct-marketing-campaigns.csv')

# Checking for missing values
print(data.isnull().sum())

"""##Feature Selection
 Uses SelectKBest to select the top 10 features for model efficiency.

"""

# Identifying numeric features for regression
numeric_columns = ['age', 'campaign', 'pdays', 'previous', 'emp.var.rate',
                   'cons.price.idx', 'cons.conf.idx', 'euribor3m', 'nr.employed']

# Applying One-Hot Encoding to categorical variables
categorical_columns = ['job', 'marital', 'education', 'default', 'housing', 'loan',
                       'contact', 'month', 'day_of_week', 'poutcome']
data_encoded = pd.get_dummies(data, columns=categorical_columns, drop_first=True)

# Binary encoding for the target variable 'y'
data_encoded['y'] = data_encoded['y'].apply(lambda x: 1 if x == 'yes' else 0)

# Selecting all features except 'y' for clustering
X = data_encoded.drop(columns=['y'])
y = data_encoded['y']

# Selecting top 10 features using SelectKBest with f_regression
selector = SelectKBest(score_func=f_regression, k=12)
X_new = selector.fit_transform(X, y)

# Getting the names of the selected features
selected_features = X.columns[selector.get_support()]
print("Selected Features:", selected_features)

"""##Prepare Data for Clustering
Scales the selected features to prepare for clustering.

"""

# Using selected features for training
X_selected = data_encoded[selected_features]

# Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_selected, y, test_size=0.2, random_state=42)

# Scaling features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Clustering analysis with K-means
clustering_features = numeric_columns + list(selected_features.difference(numeric_columns))
X_clustering = data_encoded[clustering_features]

# Scaling for clustering
X_scaled = scaler.fit_transform(X_clustering)

"""##Elbow Method
Determines the optimal number of clusters by calculating WCSS.

"""

# Elbow Method to determine optimal clusters
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)

# Plotting the Elbow Method
plt.figure(figsize=(8, 5))
plt.plot(range(1, 11), wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()

"""##K-means Clustering
Applies K-means with the optimal cluster number (3 clusters in this case).

**Cluster Center and Distribution**

Displays the cluster centers and the number of customers in each cluster.

**PCA for 2D Visualization**

Reduces dimensions with PCA and plots clusters in 2D.

"""

# Applying K-means with the selected number of clusters
optimal_clusters = 3
kmeans = KMeans(n_clusters=optimal_clusters, random_state=42)
data_encoded['Cluster'] = kmeans.fit_predict(X_scaled)

# Display the cluster centers and distribution
print("Cluster Centers:\n", kmeans.cluster_centers_)
print("\nCluster Distribution:\n", data_encoded['Cluster'].value_counts())

# PCA for 2D visualization
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# Visualize clusters in PCA-reduced space
plt.figure(figsize=(8, 5))
for cluster in range(optimal_clusters):
    plt.scatter(X_pca[data_encoded['Cluster'] == cluster, 0], X_pca[data_encoded['Cluster'] == cluster, 1], s=100, label=f'Cluster {cluster + 1}')
centroids_pca = pca.transform(kmeans.cluster_centers_)
plt.scatter(centroids_pca[:, 0], centroids_pca[:, 1], s=300, c='yellow', label='Centroids', marker='X')
plt.title('Clusters of Customers (PCA-reduced)')
plt.xlabel('PCA Component 1')
plt.ylabel('PCA Component 2')
plt.legend()
plt.show()

"""##Visualization with Original Features
 Visualizes clusters based on age and campaign contacts for further insight.

"""

# Visualization using original feature dimensions ('age' and 'campaign')
plt.figure(figsize=(8, 5))
X_visualization = X_scaled[:, [0, 1]]  # Using 'age' and 'campaign' for visualization
for cluster in range(optimal_clusters):
    plt.scatter(X_visualization[data_encoded['Cluster'] == cluster, 0], X_visualization[data_encoded['Cluster'] == cluster, 1], s=100, label=f'Cluster {cluster + 1}')
centroids = kmeans.cluster_centers_[:, [0, 1]]
plt.scatter(centroids[:, 0], centroids[:, 1], s=300, c='yellow', label='Centroids', marker='X')
plt.title('Clusters of Customers')
plt.xlabel('Age (scaled)')
plt.ylabel('Campaign Contacts (scaled)')
plt.legend()
plt.show()

"""##Unscaled Data for Visualization

X_visualization_original directly uses the original values from age and campaign without scaling.

**Inverse Transform Centroids:**

centroids_original uses the inverse_transform method on the centroids to bring them back to the original scale of age and campaign.
"""

# Visualization using original feature dimensions ('age' and 'campaign')
plt.figure(figsize=(8, 5))

# Select original 'age' and 'campaign' columns (unscaled) for visualization
X_visualization_original = data_encoded[['age', 'campaign']].values  # Unscaled data for 'age' and 'campaign'

# Inverse transform centroids to original scale
centroids_original = scaler.inverse_transform(kmeans.cluster_centers_)[:, [0, 1]]

# Plot each cluster in unscaled data
for cluster in range(optimal_clusters):
    plt.scatter(
        X_visualization_original[data_encoded['Cluster'] == cluster, 0],
        X_visualization_original[data_encoded['Cluster'] == cluster, 1],
        s=100, label=f'Cluster {cluster + 1}'
    )

# Plot centroids in unscaled space
plt.scatter(
    centroids_original[:, 0], centroids_original[:, 1],
    s=300, c='yellow', label='Centroids', marker='X'
)

plt.title('Clusters of Customers (Unscaled)')
plt.xlabel('Age')
plt.ylabel('Campaign Contacts')
plt.legend()
plt.show()

"""##Interpreting the Metrics

Silhouette Score: Values closer to 1 indicate better cluster separation.
Inertia: Lower values indicate that points are closer to their cluster centers, though this should be balanced with the number of clusters.
Davies-Bouldin Index: Lower values indicate better clustering quality.
"""

from sklearn.metrics import silhouette_score, davies_bouldin_score

# Silhouette Score
silhouette_avg = silhouette_score(X_scaled, kmeans.labels_)
print(f"Silhouette Score: {silhouette_avg:.2f}")

# Inertia (WCSS)
print(f"Inertia (WCSS): {kmeans.inertia_:.2f}")

# Davies-Bouldin Index
db_index = davies_bouldin_score(X_scaled, kmeans.labels_)
print(f"Davies-Bouldin Index: {db_index:.2f}")