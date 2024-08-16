# src/data_cleaning.py
import pandas as pd

def clean_missing_data(df, strategy='mean'):
    """Handle missing data by filling or dropping, only for numeric columns."""
    numeric_cols = df.select_dtypes(include=['number']).columns

    if strategy == 'mean':
        df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
    elif strategy == 'drop':
        df = df.dropna()
    else:
        raise ValueError("Unsupported strategy. Use 'mean' or 'drop'.")
    
    return df

def normalize_data(df):
    """Normalize data using min-max scaling."""
    return (df - df.min()) / (df.max() - df.min())

def detect_outliers(df, threshold=1.5):
    """Detect and handle outliers using the IQR method, only for numeric columns."""
    numeric_cols = df.select_dtypes(include=['number']).columns
    Q1 = df[numeric_cols].quantile(0.25)
    Q3 = df[numeric_cols].quantile(0.75)
    IQR = Q3 - Q1
    return df[~((df[numeric_cols] < (Q1 - threshold * IQR)) | (df[numeric_cols] > (Q3 + threshold * IQR))).any(axis=1)]

