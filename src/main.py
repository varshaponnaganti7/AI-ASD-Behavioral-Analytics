from visualization import plot_clusters
from data_loader import load_data
from preprocessing import clean_ethnicity, encode_target
from feature_engineering import create_behavior_features

from clustering import (
    scale_features,
    run_kmeans,
    run_pca
)


# Load dataset
df = load_data("data/Autism.csv")

# Preprocessing
df = clean_ethnicity(df)
df = encode_target(df)

# Feature engineering
df = create_behavior_features(df)

# Behavioral feature columns
behavior_cols = [
    'A1_Score', 'A2_Score', 'A3_Score',
    'A4_Score', 'A5_Score',
    'A6_Score', 'A7_Score',
    'A8_Score', 'A9_Score',
    'A10_Score'
]

# Feature matrix
X = df[behavior_cols]

# Scale features
X_scaled = scale_features(X)

# KMeans clustering
clusters = run_kmeans(X_scaled)

# Add cluster labels
df['cluster'] = clusters

# PCA dimensionality reduction
pca_df = run_pca(X_scaled)

# Add cluster labels to PCA dataframe
pca_df['cluster'] = clusters

# Preview PCA results
print(pca_df.head())

# Preview engineered features
print(df[[
    'behavior_total_score',
    'communication_score',
    'social_interaction_score',
    'behavior_variability_score'
]].head())

# Visualize clusters
plot_clusters(pca_df)