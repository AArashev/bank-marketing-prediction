
from sklearn.model_selection import train_test_split

def split_train_test_by_cluster(data, features_scaled, target, cluster_id):
    cluster_data = features_scaled[data['cluster'] == cluster_id]
    target_data = target[data['cluster'] == cluster_id]
    return train_test_split(cluster_data, target_data, test_size=0.2, random_state=42)
