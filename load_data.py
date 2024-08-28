import pandas as pd
# Step 3: Load the dataset for SARIMA analysis
file_path='daily_avg_kw_total.csv'
def load_data(file_path):
    df = pd.read_csv(file_path, parse_dates=['Date'], dayfirst=True)
    df.set_index('Date', inplace=True)
    return df