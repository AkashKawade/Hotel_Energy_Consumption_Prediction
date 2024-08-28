import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
# Step 7: Plot ACF and PACF
def plot_acf_pacf(series):
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plot_acf(series, ax=plt.gca(), lags=40)
    plt.title('ACF of Average kW (Total)')

    plt.subplot(1, 2, 2)
    plot_pacf(series, ax=plt.gca(), lags=40, method='ywm')
    plt.title('PACF of Average kW (Total)')
    plt.tight_layout()
    plt.show()