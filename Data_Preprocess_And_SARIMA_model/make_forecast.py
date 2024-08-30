import pandas as pd


# Step 10: Make predictions
def make_forecast(results, df, steps=30):
    forecast = results.get_forecast(steps=steps)
    forecast_index = pd.date_range(start=df.index[-1] + pd.Timedelta(days=1), periods=steps, freq='D')
    forecast_mean = forecast.predicted_mean
    forecast_conf_int = forecast.conf_int()

    forecast_df = pd.DataFrame({
        'Date': forecast_index,
        'Forecast': forecast_mean,
        'Lower CI': forecast_conf_int.iloc[:, 0],
        'Upper CI': forecast_conf_int.iloc[:, 1]
    })

    # Print the forecast DataFrame
    print(forecast_df)

    return forecast_df
