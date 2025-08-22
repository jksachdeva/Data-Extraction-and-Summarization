from google.cloud import storage
import pandas as pd
import json

from src.config import BUCKET_NAME, FILE_NAME

def load_news_data():
    """
    Loads news records from a JSONL file stored in a Google Cloud Storage bucket.

    Returns:
        pd.DataFrame: DataFrame containing all news records.
    """
    client = storage.Client()
    bucket = client.get_bucket(BUCKET_NAME)
    blob = bucket.blob(FILE_NAME)
    data_str = blob.download_as_string().decode('utf-8')
    records = [json.loads(line) for line in data_str.splitlines() if line.strip()]
    df = pd.DataFrame(records)
    return df
