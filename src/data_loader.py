import pandas as pd


def load_data(filepath):
    """
    Load autism screening dataset.
    """

    df = pd.read_csv(filepath)

    return df