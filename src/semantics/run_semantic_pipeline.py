from src.semantics.embed_log import embed_logs
from src.semantics.cluster_log import cluster_embeddings
import os

LOG_CSV = "data/processed/logs.csv"
OUTPUT_CSV = "data/processed/logs_with_clusters.csv"  # New output file

def main():
    # Step 1: Embed logs
    df = embed_logs(LOG_CSV)
    
    # Step 2: Cluster embeddings
    df = cluster_embeddings(df, n_clusters=3)
    
    # Step 3: Save cluster assignments
    os.makedirs(os.path.dirname(OUTPUT_CSV), exist_ok=True)
    df.to_csv(OUTPUT_CSV, index=False)
    print(f"Saved logs with cluster IDs to {OUTPUT_CSV}\n")
    
    # Step 4: Display clusters (first 3 messages per cluster)
    print("Semantic Clustering Output:\n")
    for cid in df["cluster_id"].unique():
        print(f"\nCluster {cid}:")
        samples = df[df["cluster_id"] == cid]["message"].head(3)
        for s in samples:
            print("  -", s)

if __name__ == "__main__":
    main()
