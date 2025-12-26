import numpy as np
from sklearn.cluster import AgglomerativeClustering

def cluster_embeddings(df, n_clusters=3):
    X = np.vstack(df["embedding"].values)

    clustering = AgglomerativeClustering(
        n_clusters=n_clusters,
        metric="cosine",
        linkage="average"
    )

    labels = clustering.fit_predict(X)
    df["cluster_id"] = labels

    return df
