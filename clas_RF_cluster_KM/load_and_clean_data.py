
import pandas as pd

def load_and_clean_data(file_path):
    data = pd.read_csv(file_path)
    data.dropna(inplace=True)
    data = pd.get_dummies(data, drop_first=True)
    return data
