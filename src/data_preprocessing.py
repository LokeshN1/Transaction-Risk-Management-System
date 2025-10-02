import pandas as pd

def preprocess_data(file_path):
    """
    Loads, cleans, and preprocesses the bank transaction data.
    """
    data = pd.read_csv(file_path)

    # --- Step 1: Clean all column names ---
    original_columns = data.columns
    data.columns = data.columns.str.strip().str.replace(' ', '_').str.replace('.', '', regex=False).str.upper()
    
    column_mapping = dict(zip(original_columns, data.columns))
    print("--- Column Name Cleaning ---")
    print("Original -> Cleaned:", column_mapping)
    print("--------------------------")

    # --- Step 2: Convert ALL columns used for modeling to numeric types ---
    # The 'errors='coerce'' part will turn any non-numeric values into NaN.
    data['WITHDRAWAL_AMT'] = pd.to_numeric(data['WITHDRAWAL_AMT'], errors='coerce')
    data['DEPOSIT_AMT'] = pd.to_numeric(data['DEPOSIT_AMT'], errors='coerce')
    data['BALANCE_AMT'] = pd.to_numeric(data['BALANCE_AMT'], errors='coerce')
    data['ACCOUNT_NO'] = pd.to_numeric(data['ACCOUNT_NO'], errors='coerce')
    
    # --- Step 3: Fill missing values ---
    # This will now fill any NaNs created during the numeric conversion with 0.
    data.fillna(0, inplace=True)
    
    # --- Step 4: Create new features ---
    data['TRANSACTION_AMOUNT'] = data['WITHDRAWAL_AMT'] - data['DEPOSIT_AMT']
    
    # Create a dummy risk flag based on the transaction amount
    data['RISK_FLAG'] = (data['TRANSACTION_AMOUNT'].abs() > 1000).astype(int)
    
    return data

if __name__ == '__main__':
    # Use a relative path to the data file
    csv_file_path = 'data/bank_transactions.csv'
    
    # Get the processed data
    processed_df = preprocess_data(csv_file_path)
    
    # Define features and labels from the processed data
    features = processed_df[['ACCOUNT_NO', 'TRANSACTION_AMOUNT', 'BALANCE_AMT']]
    labels = processed_df['RISK_FLAG']

    print("\n--- Example Usage Output ---")
    print("Features Head:")
    print(features.head())
    print("\nLabels Head:")
    print(labels.head())
    print("--------------------------")