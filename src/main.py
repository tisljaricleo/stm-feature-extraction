import os
import pickle
import numpy as np
import pandas as pd
from stm_features.feature_extraction import FeatureExtraction
from stm_features.visualization import plot_heatmap


def open_pickle(path):
    """
    Opens pickle data from defined path.
    :param path: Path to pickle file.
    :return:
    """
    try:
        with open(path, "rb") as handle:
            data = pickle.load(handle)
            return data
    except Exception as e:
        if hasattr(e, "message"):
            print(e.message)
            return None
        else:
            print(e)
            return None


def save_pickle_data(path, data):
    """
    Saves data in the pickle format.
    :param path: Path to save.
    :param data: Data to save.
    :return:
    """
    try:
        with open(path, "wb") as handler:
            pickle.dump(data, handler, protocol=pickle.HIGHEST_PROTOCOL)
    except Exception as e:
        if hasattr(e, "message"):
            print(e.message)
        else:
            print(e)


# path = os.getcwd()
# data_path = str(path) + r"/data/all_matrices.pkl"

from pathlib import Path

path = Path(os.getcwd()).parent.absolute()
data_path = str(path) + r"/data/all_matrices.pkl"


stms = open_pickle(data_path)

print(data_path)

data_list = []
id_ = 0
none_counter = 0

for stm in stms:
    ext = FeatureExtraction(stm["stm"])

    x, y = ext.get_mass_center()
    c = ext.get_true_class()

    if c is None:
        none_counter += 1
        continue

    data = {
        "id": id_,
        "stm": stm["stm"],
        "c_x": x,
        "c_y": y,
        "area": ext.get_p_area(),
        "p_kocenja": ext.get_p_break(),
        "p_acc": ext.get_p_acceleration(),
        "p_con": ext.get_p_congestion(),
        "p_unst": ext.get_p_unstable(),
        "p_ff": ext.get_p_freeflow(),
        "p_other": ext.get_p_other(),
        "true_class": c,
    }
    data_list.append(data)

    id_ += 1

    # plot_heatmap(ext.stm_orig, "stm")
    # print()

print(none_counter)
save_pickle_data("final_df.pkl", data_list)
print()