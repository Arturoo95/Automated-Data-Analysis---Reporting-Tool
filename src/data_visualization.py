# src/data_visualization.py
import matplotlib.pyplot as plt
import seaborn as sns

def plot_correlation_matrix(df, output_path):
    """Generate and save a correlation matrix heatmap."""
    plt.figure(figsize=(10, 8))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm', vmin=-1, vmax=1)
    plt.title('Correlation Matrix')
    plt.savefig(output_path)

def plot_histogram(df, column, output_path):
    """Generate and save a histogram for a specific column."""
    plt.figure(figsize=(8, 6))
    sns.histplot(df[column], kde=True)
    plt.title(f'Histogram of {column}')
    plt.savefig(output_path)
