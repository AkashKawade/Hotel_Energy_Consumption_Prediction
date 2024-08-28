import matplotlib.pyplot as plt
# Step 9: Diagnose the model
def diagnose_model(results):
    results.plot_diagnostics(figsize=(15, 12))
    plt.show()
