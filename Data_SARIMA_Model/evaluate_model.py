from sklearn.metrics import mean_absolute_error, mean_squared_error, mean_absolute_percentage_error

# Step 12: Model evaluation
def evaluate_model(results, df, forecast_df):
    predicted_values = results.predict(start=df.index[0], end=df.index[-1])
    mae = mean_absolute_error(df['Average kW (Total)'], predicted_values)
    mse = mean_squared_error(df['Average kW (Total)'], predicted_values)
    mape = (abs(df['Average kW (Total)'] - predicted_values) / df['Average kW (Total)']).mean() * 100

    print(f'Mean Absolute Error: {mae}')
    print(f'Mean Squared Error: {mse}')
    print(f'Mean Absolute Percentage Error: {mape}%')

    # Compare with forecasted values (out-of-sample)
    forecast_mae = mean_absolute_error(forecast_df['Forecast'], df['Average kW (Total)'].iloc[-len(forecast_df):])
    forecast_mse = mean_squared_error(forecast_df['Forecast'], df['Average kW (Total)'].iloc[-len(forecast_df):])
    forecast_mape = mean_absolute_percentage_error(forecast_df['Forecast'], df['Average kW (Total)'].iloc[-len(forecast_df):]) * 100

    print(f'Forecast MAE: {forecast_mae}')
    print(f'Forecast MSE: {forecast_mse}')
    print(f'Forecast MAPE: {forecast_mape}%')
