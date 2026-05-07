from visualization import plot_clusters
from data_loader import load_data
from preprocessing import clean_ethnicity, encode_target

from clustering import (
    scale_features,
    run_kmeans,
    run_pca
)


# Load data
df = load_data("data/Autism.csv")

# Preprocessing
df = clean_ethnicity(df)
df = encode_target(df)

# Behavioral feature columns
behavior_cols = [
    'A1_Score', 'A2_Score', 'A3_Score', 'A4_Score', 'A5_Score',
    'A6_Score', 'A7_Score', 'A8_Score', 'A9_Score', 'A10_Score'
]

# Features
X = df[behavior_cols]

# Scale features
X_scaled = scale_features(X)

# Run clustering
clusters = run_kmeans(X_scaled)

# Add clusters to dataframe
df['cluster'] = clusters

# Run PCA
pca_df = run_pca(X_scaled)

# Add cluster labels
pca_df['cluster'] = clusters

# Preview
print(pca_df.head())

# Plot clusters
plot_clusters(pca_df)