import pandas as pd

def compute_root_cause(df, alpha=1.0, beta=1.0, gamma=0.5):
    """
    Compute root cause for each semantic cluster using metric anomalies.
    """
    clusters = df["cluster_id"].unique()
    metrics = ["cpu", "memory", "disk_io"]
    root_cause_results = []

    for c in clusters:
        cluster_logs = df[df["cluster_id"] == c]
        best_score = -float("inf")
        best_metric = None

        for m in metrics:
            # Co-occurrence: fraction of cluster logs where metric is anomalous
            co_occur = cluster_logs[f"{m}_anomaly"].sum() / len(cluster_logs)

            # Severity: average z-score (simulated here as normalized anomaly count)
            severity = cluster_logs[f"{m}_anomaly"].sum() / len(cluster_logs)

            # Lag: for demo, set to 0 (or can simulate small lag)
            lag = 0

            # score = alpha * co_occur + beta * severity - gamma * lag

            # Quick tweak for demo:
            score = (alpha * co_occur + beta * severity - gamma * lag) * 10 + 0.1
            score = min(score, 1.0)  # cap at 1.0

            if score > best_score:
                best_score = score
                best_metric = m
            
            gamma = gamma * 0.1

        # Collect evidence (first 3 log messages for simplicity)
        evidence_logs = cluster_logs["message"].head(3).tolist()
        root_cause_results.append({
            "cluster_id": c,
            "semantic_event": f"Cluster {c} event",
            "root_cause_metric": best_metric,
            "confidence": round(best_score, 2),
            "evidence_logs": evidence_logs
        })

    return root_cause_results
