def clean_ethnicity(df):
    """
    Clean ethnicity column.
    """

    df['ethnicity'] = df['ethnicity'].replace({
        'others': 'Others',
        '?': 'Unknown'
    })

    df['ethnicity'] = (
        df['ethnicity']
        .str.replace("'", "", regex=False)
        .str.strip()
    )

    return df


def encode_target(df):
    """
    Encode ASD target column.
    """

    df['Class/ASD'] = df['Class/ASD'].map({
        'NO': 0,
        'YES': 1
    })

    return df