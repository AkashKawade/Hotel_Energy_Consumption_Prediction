# Step 6: Perform differencing to make the series stationary
def difference_series(df):
    df['Average kW (Total) Diff'] = df['Average kW (Total)'] - df['Average kW (Total)'].shift(1)
    df.dropna(inplace=True)
    return df
