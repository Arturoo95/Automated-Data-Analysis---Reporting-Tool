# src/data_analysis.py
import pandas as pd

def summarize_data(df):
    """Generate summary statistics."""
    return df.describe()

def group_data(df, by_column):
    """Group data by a specific column."""
    return df.groupby(by_column).mean()

def correlation_matrix(df):
    """Compute the correlation matrix."""
    return df.corr()
