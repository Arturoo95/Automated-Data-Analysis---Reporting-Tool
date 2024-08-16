# tests/test_data_analysis.py
import unittest
import pandas as pd
from src.data_analysis import summarize_data, group_data, correlation_matrix

class TestDataAnalysis(unittest.TestCase):

    def setUp(self):
        # Sample DataFrame
        self.df = pd.DataFrame({
            'Category': ['A', 'A', 'B', 'B', 'C'],
            'Value1': [10, 20, 10, 30, 50],
            'Value2': [100, 200, 100, 300, 500]
        })

    def test_summarize_data(self):
        summary = summarize_data(self.df[['Value1', 'Value2']])
        self.assertEqual(summary.loc['mean', 'Value1'], 24)
        self.assertEqual(summary.loc['mean', 'Value2'], 240)

    def test_group_data(self):
        grouped = group_data(self.df, 'Category')
        self.assertEqual(grouped.loc['A', 'Value1'], 15)
        self.assertEqual(grouped.loc['B', 'Value1'], 20)
        self.assertEqual(grouped.loc['C', 'Value1'], 50)

    def test_correlation_matrix(self):
        corr = correlation_matrix(self.df[['Value1', 'Value2']])
        self.assertAlmostEqual(corr.loc['Value1', 'Value2'], 1.0, places=5)

if __name__ == '__main__':
    unittest.main()
