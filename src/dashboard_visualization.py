import plotly.express as px
import pandas as pd # Import pandas to handle data manipulation

def create_dashboard(data):
    """
    Creates an improved interactive dashboard using Plotly.
    """
    print("\nGenerating improved interactive dashboard...")

    # --- Step 1: Convert DATE column to a proper datetime format ---
    # This is essential for correct sorting and plotting over time.
    data['DATE'] = pd.to_datetime(data['DATE'])

    # --- Step 2: Sort the data by date ---
    # This is the most important fix to prevent the "spaghetti" plot.
    data.sort_values(by='DATE', inplace=True)

    # --- Step 3: Aggregate data for a cleaner plot (Optional but Recommended) ---
    # Instead of plotting every single transaction, we can group by day
    # and sum the transaction amounts to see the net flow per day.
    daily_summary = data.groupby('DATE')['TRANSACTION_AMOUNT'].sum().reset_index()

    # --- Step 4: Create the improved plot using the aggregated data ---
    fig = px.line(
        daily_summary, 
        x='DATE', 
        y='TRANSACTION_AMOUNT', 
        title='Net Transaction Amount per Day',
        labels={'DATE': 'Date', 'TRANSACTION_AMOUNT': 'Net Transaction Amount'} # Add clearer labels
    )

    # --- Step 5: Add interactive features ---
    # A range slider is very useful for time-series data.
    fig.update_xaxes(rangeslider_visible=True)

    fig.show()