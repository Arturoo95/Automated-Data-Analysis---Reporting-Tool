import yaml
import os
import pandas as pd
from src.data_cleaning import clean_missing_data, normalize_data, detect_outliers
from src.data_analysis import summarize_data, correlation_matrix
from src.data_visualization import plot_correlation_matrix, plot_histogram
from src.report_generation import generate_pdf_report

def load_config():
    """Load configuration settings from config.yaml."""
    config_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'config.yaml')
    with open(config_path, 'r') as file:
        return yaml.safe_load(file)

def run_analysis():
    config = load_config()

    # Load Data
    df = pd.read_csv(config['data_path'])

    # Clean Data
    df = clean_missing_data(df)
    df = detect_outliers(df)

    # Analyze Data
    summary = summarize_data(df[['Quantity', 'Price', 'Total_Sale']])
    corr_matrix = correlation_matrix(df[['Quantity', 'Price', 'Total_Sale']])

    # Visualize Data
    plot_histogram(df, 'Total_Sale', config['plots']['histogram'])
    plot_correlation_matrix(df[['Quantity', 'Price', 'Total_Sale']], config['plots']['correlation_matrix'])

    # Generate Report
    generate_pdf_report(
        summary,
        [config['plots']['correlation_matrix'], config['plots']['histogram']],
        config['output_report_path']
    )

if __name__ == "__main__":
    run_analysis()

