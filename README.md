# IoT Sensor Data Processing

## Overview
This project focuses on **processing and analyzing IoT sensor data** using Python.  
It simulates how raw sensor readings can be cleaned, transformed, and analyzed to extract meaningful insights for monitoring and decision-making.

The project demonstrates a basic end-to-end IoT data pipeline:
- Data ingestion
- Preprocessing
- Feature extraction
- Simple analysis and visualization

---

## Problem Statement
IoT devices generate continuous streams of raw sensor data that often contain:
- Noise
- Missing values
- Irregular sampling

This project aims to:
- Process raw sensor readings
- Clean and structure the data
- Perform basic statistical analysis
- Prepare data for further ML or monitoring systems

---

## Key Features
- Reads IoT sensor data from input files or simulated streams
- Cleans and normalizes sensor values
- Handles missing or corrupted data
- Computes summary statistics
- Visualizes sensor trends

---

## How It Works

### 1. Data Ingestion
Sensor data is loaded from a file (e.g., CSV) containing time-series readings.

### 2. Preprocessing
The data is:
- Stripped of invalid values
- Converted into structured format
- Normalized for analysis

### 3. Analysis
The system computes:
- Mean, max, min sensor values
- Trend patterns over time
- Basic anomaly indicators

---

## Tech Stack
- Python  
- Pandas  
- NumPy  
- Matplotlib  

---

## How to Run

1. Install dependencies:
```bash
pip install -r requirements.txt
