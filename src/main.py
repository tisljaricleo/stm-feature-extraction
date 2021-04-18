import os
from stm_features import extract_features
from ml_algorithms import get_comparison

# path = os.getcwd()
# data_path = str(path) + r"/data/all_matrices.pkl"
# save_path = str(path) + r"/data/final_dataframe.pkl"

from pathlib import Path

path = Path(os.getcwd()).parent.absolute()
data_path = str(path) + r"/data/all_matrices.pkl"
save_path = str(path) + r"/data/final_dataframe.pkl"

print("Starting with feature extraction...")
extract_features(data_path, save_path)

print("Starting to compare algorithms...")
get_comparison(save_path)
