import pandas as pd
import os
import logging

logging.basicConfig(level=logging.INFO)


def load_csv(path, columns):
    if not os.path.exists(path):
        df = pd.DataFrame(columns=columns)
        df.to_csv(path, index=False)
        return df

    try:
        df = pd.read_csv(path)

        if df.empty:
            return pd.DataFrame(columns=columns)

        return df

    except Exception as e:
        logging.error(f"Failed to load CSV: {str(e)}")
        return pd.DataFrame(columns=columns)


def save_csv(path, df):
    try:
        df.to_csv(path, index=False)
    except Exception as e:
        logging.error(f"Failed to save CSV: {str(e)}")