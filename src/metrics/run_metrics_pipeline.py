from src.metrics.simulate_metrics import simulate_metrics
from src.metrics.detect_anomalies import detect_anomalies

LOG_CSV = "data/processed/logs_with_clusters.csv"

def main():
    df = simulate_metrics(LOG_CSV)
    df = detect_anomalies(df)

    # Print summary
    print("Metric anomaly counts:")
    print(df[["cpu_anomaly", "memory_anomaly", "disk_io_anomaly"]].sum())

    # Save for correlation
    df.to_csv("data/processed/logs_with_metrics.csv", index=False)
    print("Saved logs + metrics for Layer 3 correlation.")

if __name__ == "__main__":
    main()
