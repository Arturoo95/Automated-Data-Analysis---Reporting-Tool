# src/report_generation.py
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def generate_pdf_report(summary, plots, output_path):
    """Create a PDF report with summary stats and plots."""
    c = canvas.Canvas(output_path, pagesize=A4)
    width, height = A4

    # Add Title
    c.setFont("Helvetica-Bold", 24)
    c.drawString(100, height - 100, "Data Analysis Report")

    # Add Summary Stats
    c.setFont("Helvetica", 12)
    c.drawString(100, height - 150, "Summary Statistics:")
    for i, (col, stats) in enumerate(summary.items()):
        text = f"{col}: Mean={stats['mean']:.2f}, Std={stats['std']:.2f}"
        c.drawString(100, height - 170 - (i * 20), text)

    # Add Plots
    for i, plot in enumerate(plots):
        c.drawImage(plot, 100, height - 300 - (i * 150), width=400, height=100)

    c.save()
