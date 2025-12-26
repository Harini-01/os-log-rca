import pandas as pd
from sentence_transformers import SentenceTransformer

def embed_logs(csv_path):
    df = pd.read_csv(csv_path)

    model = SentenceTransformer("all-MiniLM-L6-v2")

    messages = df["message"].tolist()
    embeddings = model.encode(messages, show_progress_bar=True)

    df["embedding"] = list(embeddings)

    return df
