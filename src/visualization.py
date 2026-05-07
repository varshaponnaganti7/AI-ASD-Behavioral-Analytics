import matplotlib.pyplot as plt
import seaborn as sns


def plot_clusters(pca_df):
    """
    Visualize behavioral clusters using PCA.
    """

    plt.figure(figsize=(10, 7))

    sns.scatterplot(
        data=pca_df,
        x='PCA1',
        y='PCA2',
        hue='cluster',
        palette='Set1'
    )

    plt.title("Behavioral Clusters (PCA Visualization)")

    plt.show()