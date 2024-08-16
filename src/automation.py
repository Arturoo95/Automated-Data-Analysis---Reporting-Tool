# src/automation.py
import schedule
import time
from src.main import run_analysis

def job():
    """Job to run the analysis and generate a report."""
    run_analysis()

def schedule_jobs():
    """Schedule the job at regular intervals."""
    schedule.every().monday.at("08:00").do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)
