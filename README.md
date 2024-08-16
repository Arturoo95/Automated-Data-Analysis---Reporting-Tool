# Overview
This project is a Python-based tool designed to automate data analysis and report generation. The tool takes raw data, performs cleaning and analysis, generates visualizations, and compiles everything into a professional report.

# Features 
Data Cleaning: Handles missing data and detects outliers.
Data Analysis: Summarizes data, calculates correlations, and performs grouping.
Visualization: Generates histograms and correlation matrices.
Report Generation: Compiles results and visualizations into a PDF report.
Automation: Can be scheduled to run at regular intervals.

# Setup and Installation
1) Clone the repository:

git clone https://github.com/Arturoo95/Automated-Data-Analysis-Reporting-Tool -
cd automated-data-analysis-tool -

2) Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate       # On Windows use `venv\Scripts\activate`

3) Install dependencies:

pip install -r requirements.txt

4) Configure the tool:

Edit the config/config.yaml file to specify the paths for input data, output reports, and any other settings.

# Usage
To run the analysis and generate a report, execute the following command:

python -m src.main
This will process the data specified in the config.yaml file and generate a report in the reports/ directory.

# Running Tests
To run the unit tests, use:

python -m unittest discover -s tests

# Contributing
Feel free to fork this repository, create a new branch, and submit a pull request with your improvements.

# License
This project is licensed under the MIT License.
