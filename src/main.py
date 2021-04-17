import os
import pickle
import numpy as np
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


# from pathlib import Path
# aaa = Path(os.getcwd()).parent.absolute()

path = os.getcwd()
data_path = str(path) + r"/data/all_matrices.pkl"
stms = open_pickle(data_path)

for stm in stms:
    ext = FeatureExtraction(stm["stm"])

    x, y = ext.get_mass_center()
    velicina = ext.get_p_area()
    p_kocenja = ext.get_p_break()
    p_acc = ext.get_p_acceleration()
    p_con = ext.get_p_congestion()
    p_unst = ext.get_p_unstable()
    p_ff = ext.get_p_freeflow()
    p_other = ext.get_p_other()

    plot_heatmap(ext.stm_orig, "stm")
    print()


print()