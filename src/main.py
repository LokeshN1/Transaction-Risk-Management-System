from src.data_preprocessing import preprocess_data
from src.risk_detection import train_risk_model
from src.dashboard_visualization import create_dashboard
from src.alerts import send_alert
import pandas as pd

# 1. Data Preprocessing
# This function now returns the entire cleaned and feature-engineered DataFrame
processed_data = preprocess_data('data/bank_transactions.csv')

# Define features and labels from the processed data using the NEW, CLEANED column names
features = processed_data[['ACCOUNT_NO', 'TRANSACTION_AMOUNT', 'BALANCE_AMT']]
labels = processed_data['RISK_FLAG']

# 2. Risk Detection Algorithm
model = train_risk_model(features, labels)

# 3. Data Integration (This step is complete after preprocessing)
# The 'processed_data' DataFrame is ready for use.

# 4. Dashboard Visualization
create_dashboard(processed_data)

# 5. Reporting (Run reporting.R script separately)
# The R script needs to be executed manually or via an automated process.
print("\nTo generate the static report, please run: Rscript src/reporting.R")

# 6. Alerts (Note: This will fail without real SMTP credentials)
try:
    print("\nAttempting to send an alert...")
    send_alert('lokeshnegi399@gmail.com', 'High Risk Alert', 'A high-risk event has been detected.')
    print("Alert function executed (check server logs for delivery status).")
except Exception as e:
    print(f"Could not send alert. Error: {e}")
    print("Please configure SMTP details in src/alerts.py")


print("\nRisk Management System Workflow Completed")