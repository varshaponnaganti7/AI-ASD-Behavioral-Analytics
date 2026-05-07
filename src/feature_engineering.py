def create_behavior_features(df):
    """
    Create engineered behavioral features.
    """

    # Total behavior score
    behavior_cols = [
        'A1_Score', 'A2_Score', 'A3_Score', 'A4_Score', 'A5_Score',
        'A6_Score', 'A7_Score', 'A8_Score', 'A9_Score', 'A10_Score'
    ]

    df['behavior_total_score'] = df[behavior_cols].sum(axis=1)

    # Communication-related indicators
    df['communication_score'] = (
        df['A1_Score'] +
        df['A7_Score'] +
        df['A10_Score']
    )

    # Social interaction indicators
    df['social_interaction_score'] = (
        df['A2_Score'] +
        df['A4_Score'] +
        df['A8_Score']
    )

    # Behavioral variability / repetitive indicators
    df['behavior_variability_score'] = (
        df['A3_Score'] +
        df['A5_Score'] +
        df['A6_Score'] +
        df['A9_Score']
    )

    return df