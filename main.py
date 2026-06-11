import random
import csv
import time
import os
from datetime import datetime
import requests

# ==========================================
# CONFIGURATION
# ==========================================

CHANNEL_API_KEY = "Yyour_write_api-key"  # ThingSpeak Write API Key
TARIFF = 8  # ₹ per kWh

energy_kwh = 0

# ==========================================
# CREATE DATA DIRECTORY
# ==========================================

os.makedirs("data", exist_ok=True)

CSV_FILE = "data/energy_log.csv"

# ==========================================
# THINGSPEAK FUNCTION
# ==========================================

def upload_to_thingspeak(voltage, current, power, energy, cost, alert):

    url = "https://api.thingspeak.com/update"

    payload = {
        "api_key": CHANNEL_API_KEY,
        "field1": round(voltage, 2),
        "field2": round(current, 2),
        "field3": round(power, 2),
        "field4": round(energy, 4),
        "field5": round(cost, 2),
        "field6": 1 if alert == "OVERLOAD" else 0
    }

    try:
        response = requests.post(url, data=payload, timeout=10)

        if response.status_code == 200:
            print("✓ ThingSpeak Updated")
        else:
            print("✗ ThingSpeak Upload Failed")

    except Exception as e:
        print("Upload Error:", e)

# ==========================================
# MAIN PROGRAM
# ==========================================

with open(CSV_FILE, mode="w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow([
        "Timestamp",
        "Voltage",
        "Current",
        "Power",
        "Energy",
        "Cost",
        "Alert"
    ])

    print("\n⚡ Smart Home Energy Monitoring Started...\n")

    try:

        while True:

            # Simulated Voltage
            voltage = random.uniform(220, 240)

            # Simulated Current
            current = random.uniform(0.5, 10)

            # Power Calculation
            power = voltage * current

            # Energy Calculation
            energy_kwh += power / 1000 * (15 / 3600)

            # Cost Calculation
            cost = energy_kwh * TARIFF

            # Alert Logic
            alert = "NORMAL"

            if power > 1500:
                alert = "OVERLOAD"

            timestamp = datetime.now()

            print("\n===================================")
            print("Timestamp :", timestamp)
            print("Voltage   :", round(voltage, 2), "V")
            print("Current   :", round(current, 2), "A")
            print("Power     :", round(power, 2), "W")
            print("Energy    :", round(energy_kwh, 4), "kWh")
            print("Cost      : ₹", round(cost, 2))
            print("Alert     :", alert)
            print("===================================")

            # Save To CSV
            writer.writerow([
                timestamp,
                round(voltage, 2),
                round(current, 2),
                round(power, 2),
                round(energy_kwh, 4),
                round(cost, 2),
                alert
            ])

            file.flush()

            # Upload To ThingSpeak
            upload_to_thingspeak(
                voltage,
                current,
                power,
                energy_kwh,
                cost,
                alert
            )

            # ThingSpeak Free Account Limit
            time.sleep(15)

    except KeyboardInterrupt:

        print("\n\nMonitoring Stopped Successfully")
        print(f"CSV Saved At: {CSV_FILE}")
