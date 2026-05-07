from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

import pandas as pd


def scale_features(X):
    """
    Scale behavioral features.
    """

    scaler = StandardScaler()

    X_scaled = scaler.fit_transform(X)

    return X_scaled


def run_kmeans(X_scaled, n_clusters=3):
    """
    Train KMeans clustering model.
    """

    kmeans = KMeans(
        n_clusters=n_clusters,
        random_state=42,
        n_init=10
    )

    clusters = kmeans.fit_predict(X_scaled)

    return clusters


def run_pca(X_scaled):
    """
    Reduce dimensions using PCA.
    """

    pca = PCA(n_components=2)

    X_pca = pca.fit_transform(X_scaled)

    pca_df = pd.DataFrame({
        'PCA1': X_pca[:, 0],
        'PCA2': X_pca[:, 1]
    })

    return pca_df