
import matplotlib.pyplot as plt
import seaborn as sns

def visualize_clusters(data, column_name='cluster'):
    plt.figure(figsize=(8, 6))
    sns.countplot(x=data[column_name])
    plt.title('Distribution of Clusters')
    plt.xlabel('Cluster')
    plt.ylabel('Count')
    plt.show()
