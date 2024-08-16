# tests/test_report_generation.py
import unittest
import os
from PIL import Image
from src.report_generation import generate_pdf_report

class TestReportGeneration(unittest.TestCase):

    def setUp(self):
        # Sample summary statistics
        self.summary = {
            'A': {'mean': 3.0, 'std': 1.414},
            'B': {'mean': 7.0, 'std': 1.414}
        }
        self.plots = ['tests/plot1.png', 'tests/plot2.png']

        # Create dummy image files
        for plot in self.plots:
            image = Image.new('RGB', (100, 100), color = (73, 109, 137))
            image.save(plot)

        self.output_pdf_path = 'tests/analysis_report_test.pdf'

    def tearDown(self):
        # Clean up generated files after each test
        if os.path.exists(self.output_pdf_path):
            os.remove(self.output_pdf_path)
        for plot in self.plots:
            if os.path.exists(plot):
                os.remove(plot)

    def test_generate_pdf_report(self):
        generate_pdf_report(self.summary, self.plots, self.output_pdf_path)
        self.assertTrue(os.path.exists(self.output_pdf_path))

if __name__ == '__main__':
    unittest.main()
