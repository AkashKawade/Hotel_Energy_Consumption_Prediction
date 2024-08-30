
import matplotlib.pyplot as plt
# Step 11: Visualize forecast
def visualize_forecast(df, forecast_df):
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df['Average kW (Total)'], label='Historical Data')
    plt.plot(forecast_df['Date'], forecast_df['Forecast'], label='Forecast', color='red')
    plt.fill_between(forecast_df['Date'],
                     forecast_df['Lower CI'],
                     forecast_df['Upper CI'], color='red', alpha=0.3)
    plt.xlabel('Date')
    plt.ylabel('Average kW (Total)')
    plt.title('SARIMA Forecast for Average kW (Total)')
    plt.legend()
    plt.show()
