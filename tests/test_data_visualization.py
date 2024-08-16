# tests/test_data_visualization.py
import unittest
import os
import pandas as pd
from src.data_visualization import plot_correlation_matrix, plot_histogram

class TestDataVisualization(unittest.TestCase):

    def setUp(self):
        # Sample DataFrame
        self.df = pd.DataFrame({
            'A': [1, 2, 3, 4, 5],
            'B': [5, 6, 7, 8, 9]
        })
        self.corr_matrix_path = 'tests/correlation_matrix_test.png'
        self.histogram_path = 'tests/histogram_test.png'

    def tearDown(self):
        # Clean up generated files after each test
        if os.path.exists(self.corr_matrix_path):
            os.remove(self.corr_matrix_path)
        if os.path.exists(self.histogram_path):
            os.remove(self.histogram_path)

    def test_plot_correlation_matrix(self):
        plot_correlation_matrix(self.df, self.corr_matrix_path)
        self.assertTrue(os.path.exists(self.corr_matrix_path))

    def test_plot_histogram(self):
        plot_histogram(self.df, 'A', self.histogram_path)
        self.assertTrue(os.path.exists(self.histogram_path))

if __name__ == '__main__':
    unittest.main()
