# Transaction Risk Management System

This project is an end-to-end system designed to analyze bank transaction data, identify potentially high-risk activities using a machine learning model, and visualize the results.

---

## Overview
The system automates the process of financial risk detection. It:
- Reads raw transaction data from a CSV file  
- Cleans and preprocesses the data  
- Trains a **Random Forest** model to flag suspicious transactions  
- Provides tools for analysis and alerting  


---

## Features
- **Data Preprocessing**: Cleans messy column names and converts data to numeric types.  
- **Machine Learning Model**: Trains a `RandomForestClassifier` to predict high-risk transactions and evaluates performance.  
- **Interactive Dashboard**: Generates time-series charts with **Plotly** to visualize transaction trends and daily net flow.  
- **Static Reporting**: Creates `risk_report.png` using **R** and **ggplot2**, suitable for formal reports.  
- **Email Alerts**: Sends notifications when high-risk events are detected.  

---

## Tech Stack
- **Languages**: Python, R  
- **Data Science & ML**: pandas, scikit-learn  
- **Visualization**: Plotly, ggplot2  
- **System & Tools**: smtplib (email alerts)  

---

## How to Run

### 1. Prerequisites
- Python **3.x** installed  
- R installed and added to your system's **PATH**  

---

### 2. Setup

```bash
# Clone the repository
git clone https://github.com/LokeshN1/Transaction-Risk-Management-System.git
cd Transaction-Risk-Management-System

# Create and activate Python virtual environment
python -m venv .venv
# On Windows
.\.venv\Scripts\activate
# On macOS/Linux
source .venv/bin/activate

# Install Python dependencies
pip install -r requirements.txt
````

Install **R dependencies**:

```r
# Start the R console
R

# Inside R console
install.packages("ggplot2")

# Quit R session
q()
```

---

### 3. Execution

Run the main application:

```bash
python -m src.main
```


