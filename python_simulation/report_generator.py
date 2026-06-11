import pandas as pd
from fpdf import FPDF

# Read CSV
df = pd.read_csv("data/energy_log.csv")

# Statistics
avg_voltage = round(df["Voltage"].mean(), 2)
avg_current = round(df["Current"].mean(), 2)
peak_power = round(df["Power"].max(), 2)
total_energy = round(df["Energy"].max(), 4)
estimated_cost = round(df["Cost"].max(), 2)

# Create PDF
pdf = FPDF()

pdf.add_page()

pdf.set_font("Arial", "B", 16)

pdf.cell(
    200,
    10,
    txt="Smart Home Energy Monitoring Report",
    ln=True,
    align="C"
)

pdf.ln(10)

pdf.set_font("Arial", size=12)

pdf.cell(200,10,f"Average Voltage: {avg_voltage} V",ln=True)
pdf.cell(200,10,f"Average Current: {avg_current} A",ln=True)
pdf.cell(200,10,f"Peak Power: {peak_power} W",ln=True)
pdf.cell(200,10,f"Total Energy: {total_energy} kWh",ln=True)
pdf.cell(200,10,f"Estimated Cost: Rs {estimated_cost}",ln=True)

pdf.output("reports/energy_report.pdf")

print("PDF Report Generated Successfully")