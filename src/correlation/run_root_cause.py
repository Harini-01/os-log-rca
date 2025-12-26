import pandas as pd
from src.correlation.root_cause import compute_root_cause

CSV_PATH = "data/processed/logs_with_metrics.csv"

def main():
    df = pd.read_csv(CSV_PATH)
    results = compute_root_cause(df)

    print("\n=== Root Cause Analysis Output ===\n")
    for r in results:
        print(f"Cluster {r['cluster_id']}:")
        print(f"  Semantic Event: {r['semantic_event']}")
        print(f"  Root Cause Metric: {r['root_cause_metric']}")
        print(f"  Confidence: {r['confidence']}")
        print(f"  Evidence Logs: ")
        for msg in r["evidence_logs"]:
            print("   -", msg)
        print()

if __name__ == "__main__":
    main()
