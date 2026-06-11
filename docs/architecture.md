# System Architecture

## Overview

The Smart Home Energy Monitoring System is an IoT-based solution that monitors electrical parameters such as voltage, current, power consumption, energy usage, electricity cost, and overload conditions.

The system uses ESP32 simulation, Python data processing, ThingSpeak cloud services, and a Streamlit dashboard for real-time visualization.

---

## Architecture Diagram

```text
┌─────────────────────┐
│ Voltage Sensor      │
│ (Simulated Input)   │
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│ Current Sensor      │
│ (Simulated Input)   │
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│ ESP32 Controller    │
│ Wokwi Simulation    │
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│ Python Processing   │
│ main.py             │
└─────────┬───────────┘
          │
    ┌─────┴─────┐
    ▼           ▼
┌─────────┐ ┌─────────────┐
│ CSV Log │ │ ThingSpeak  │
│ Storage │ │ Cloud       │
└────┬────┘ └──────┬──────┘
     │             │
     ▼             ▼
┌────────────────────────┐
│ Streamlit Dashboard    │
│ Data Visualization     │
└────────────────────────┘
```

---

## System Workflow

### Step 1: Data Generation

Voltage and current values are generated through simulation.

Example:

- Voltage: 220V – 240V
- Current: 0.5A – 10A

---

### Step 2: Power Calculation

Power is calculated using:

P = V × I

Where:

- P = Power (W)
- V = Voltage (V)
- I = Current (A)

---

### Step 3: Energy Calculation

Energy consumption is calculated continuously.

Energy (kWh) = Power × Time

---

### Step 4: Cost Estimation

Electricity cost is estimated using:

Cost = Energy × Tariff

Current tariff:

₹8 per kWh

---

### Step 5: Overload Detection

The system checks whether power exceeds the threshold.

```python
if power > 1500:
    alert = "OVERLOAD"
else:
    alert = "NORMAL"
```

---

### Step 6: Local Data Logging

Data is stored in:

```text
data/energy_log.csv
```

Stored fields:

- Timestamp
- Voltage
- Current
- Power
- Energy
- Cost
- Alert

---

### Step 7: Cloud Upload

Data is uploaded to ThingSpeak every 15 seconds.

Fields:

| ThingSpeak Field | Parameter |
|-----------------|-----------|
| Field 1 | Voltage |
| Field 2 | Current |
| Field 3 | Power |
| Field 4 | Energy |
| Field 5 | Cost |
| Field 6 | Alert |

---

### Step 8: Dashboard Visualization

Streamlit reads CSV data and displays:

- Voltage Trends
- Current Trends
- Power Consumption
- Energy Usage
- Electricity Cost
- Alert Status
- Historical Data

---

## Components Used

### Hardware

- ESP32 Development Board
- Voltage Sensor (Simulated)
- Current Sensor (Simulated)
- LED Indicators
- Buzzer

### Software

- Python
- Streamlit
- ThingSpeak
- Wokwi
- CSV
- GitHub

---

## Key Features

- Real-Time Monitoring
- Cloud Integration
- Cost Estimation
- Overload Alerts
- Interactive Dashboard
- Historical Data Storage
- IoT Simulation

---

## Future Enhancements

- MQTT Communication
- Mobile Application
- AI-Based Energy Prediction
- Smart Meter Integration
- Email Alerts
- SMS Notifications
- Home Automation Support