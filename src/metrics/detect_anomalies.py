import pandas as pd

def detect_anomalies(df, z_thresh=2.0):
    """
    Detect anomalies in metrics using z-score method.
    Returns dataframe with anomaly flags.
    """
    metrics = ["cpu", "memory", "disk_io"]
    for m in metrics:
        mean = df[m].mean()
        std = df[m].std()
        df[f"{m}_anomaly"] = ((df[m] - mean).abs() > z_thresh * std).astype(int)
    return df
