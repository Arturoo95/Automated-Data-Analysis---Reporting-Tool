# tests/test_data_cleaning.py
import unittest
import pandas as pd
from src.data_cleaning import clean_missing_data, normalize_data, detect_outliers

class TestDataCleaning(unittest.TestCase):

    def setUp(self):
        # Sample DataFrame
        self.df = pd.DataFrame({
            'A': [1, 2, None, 4, 5],
            'B': [10, None, 30, 40, 50],
            'C': [None, 1, None, 2, 3]
        })

    def test_clean_missing_data(self):
        cleaned_df = clean_missing_data(self.df, strategy='mean')
        self.assertFalse(cleaned_df.isnull().values.any())

    def test_normalize_data(self):
        normalized_df = normalize_data(self.df.fillna(0))
        self.assertTrue(normalized_df.max().max() <= 1)
        self.assertTrue(normalized_df.min().min() >= 0)

    def test_detect_outliers(self):
        df_with_outliers = self.df.copy()
        df_with_outliers.loc[0, 'A'] = 1000  # Adding an outlier
        cleaned_df = detect_outliers(df_with_outliers)
        self.assertTrue(1000 not in cleaned_df['A'].values)

if __name__ == '__main__':
    unittest.main()
