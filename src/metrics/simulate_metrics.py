import pandas as pd
import numpy as np

def simulate_metrics(log_csv="data/processed/logs.csv"):
    """
    Generate simulated CPU, memory, disk I/O metrics aligned with log timestamps.
    """
    df = pd.read_csv(log_csv)
    np.random.seed(42)

    # Simulate metrics
    df["cpu"] = np.random.normal(loc=20, scale=5, size=len(df))  # % CPU
    df["memory"] = np.random.normal(loc=40, scale=10, size=len(df))  # % RAM
    df["disk_io"] = np.random.normal(loc=50, scale=15, size=len(df))  # arbitrary units

    return df
