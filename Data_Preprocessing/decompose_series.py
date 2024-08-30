from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib.pyplot as plt
# Step 4: Perform time series decomposition
def decompose_series(df):
    decomposition = seasonal_decompose(df['Average kW (Total)'], model='additive', period=7)
    trend = decomposition.trend
    seasonal = decomposition.seasonal
    residual = decomposition.resid

    plt.figure(figsize=(12, 8))
    plt.subplot(411)
    plt.plot(df.index, df['Average kW (Total)'], label='Original')
    plt.legend(loc='upper left')
    plt.subplot(412)
    plt.plot(df.index, trend, label='Trend')
    plt.legend(loc='upper left')
    plt.subplot(413)
    plt.plot(df.index, seasonal, label='Seasonality')
    plt.legend(loc='upper left')
    plt.subplot(414)
    plt.plot(df.index, residual, label='Residuals')
    plt.legend(loc='upper left')
    plt.tight_layout()
    plt.show()