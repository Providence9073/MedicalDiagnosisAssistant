import pandas as pd
import os

def load_data(filename):
    filepath = os.path.join(os.path.dirname(__file__), '..', 'data', filename)
    df = pd.read_csv(filepath)
    return df

