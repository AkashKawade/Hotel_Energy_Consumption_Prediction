from statsmodels.tsa.statespace.sarimax import SARIMAX
from pmdarima import auto_arima
import matplotlib.pyplot as plt

# Step 8: Fit a SARIMA model
def fit_sarima_model(df):
    auto_model = auto_arima(df['Average kW (Total)'],
                            start_p=1, start_q=1,
                            max_p=3, max_q=3, m=7,
                            start_P=0, seasonal=True,
                            d=1, D=1, trace=True,
                            error_action='ignore',
                            suppress_warnings=True,
                            stepwise=True)
    print(auto_model.summary())

    model = SARIMAX(df['Average kW (Total)'],
                    order=auto_model.order,
                    seasonal_order=auto_model.seasonal_order,
                    enforce_stationarity=False,
                    enforce_invertibility=False)

    results = model.fit()
    return results


