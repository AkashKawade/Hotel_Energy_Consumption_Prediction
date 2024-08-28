import pandas as pd
# Step 2: Load the CSV and calculate daily averages
file_path = 'Hotel_Data_combined_Aug23toAug24.csv'
def calculate_daily_averages(file_path):
    df = pd.read_csv(file_path)
    df['Date'] = pd.to_datetime(df['Date'])

    # Group by the date and calculate the average of 'kW (Total)' for each day
    daily_avg_df = df.groupby(df['Date'].dt.date)['kW (Total)'].mean().reset_index()
    daily_avg_df.columns = ['Date', 'Average kW (Total)']

    # Save the daily averages to a new CSV file
    csv_file_path = 'daily_avg_kw_total.csv'
    daily_avg_df.to_csv(csv_file_path, index=False)
    return csv_file_path
