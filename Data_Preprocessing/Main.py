from load_data import load_data
from decompose_series import decompose_series
from Data_SARIMA_Model.check_stationarity import check_stationarity
from difference_series import difference_series
from plot_acf_pacf import plot_acf_pacf
from fit_sarima_model import fit_sarima_model
from make_forecast import make_forecast
from evaluate_model import evaluate_model
from visualize_forecast import visualize_forecast
from load_and_combine_excel import load_and_combine_excel
from calculate_daily_averages import calculate_daily_averages
from Data_SARIMA_Model.diagnose_model import diagnose_model

def main():
    # Step 1: Load and process Excel data, then save combined CSV
    excel_file_path = 'Hourly_report_Main Kitchen + Cold Storage_Wed Aug 23 2023_to_Fri Aug 23 2024 (1).xlsx'  # Replace with your Excel file path
    csv_combined_path = load_and_combine_excel(excel_file_path)

    # Step 2: Calculate daily averages and save to a new CSV
    csv_daily_avg_path = calculate_daily_averages(csv_combined_path)

    # Step 3: Load the processed dataset for SARIMA analysis
    df = load_data(csv_daily_avg_path)

    # Step 4: Decompose the series into trend, seasonality, and residual components
    decompose_series(df)

    # Step 5: Check for stationarity using ADF test
    p_value = check_stationarity(df['Average kW (Total)'])

    # Step 6: Perform differencing if the series is non-stationary
    if p_value > 0.05:
        df = difference_series(df)

    # Step 7: Plot ACF and PACF to determine ARIMA model parameters
    plot_acf_pacf(df['Average kW (Total) Diff'] if p_value > 0.05 else df['Average kW (Total)'])

    # Step 8: Fit a SARIMA model
    results = fit_sarima_model(df)

    # Step 9: Diagnose the model
    diagnose_model(results)

    # Step 10: Make predictions (forecast)
    forecast_steps = 30  # Change the number of steps as needed
    forecast_df = make_forecast(results, df, steps=forecast_steps)

    # Step 11: Visualize the forecast
    visualize_forecast(df, forecast_df)

    # Step 12: Evaluate the model performance
    evaluate_model(results, df, forecast_df)


if __name__ == "__main__":
    main()

