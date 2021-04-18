from stm_features.feature_extraction import FeatureExtraction
from stm_features.misc import open_pickle
import pandas as pd


def extract_features(data_path: str, save_path: str):
    """Extract defined features from STM using FeatureExtraction class

    Args:
        data_path (str): Path to STMs (pickle data)
        save_path (str): Path for saving the results
    """
    stms = open_pickle(data_path)

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
            "p_break": ext.get_p_break(),
            "p_acc": ext.get_p_acceleration(),
            "p_con": ext.get_p_congestion(),
            "p_unst": ext.get_p_unstable(),
            "p_ff": ext.get_p_freeflow(),
            "p_other": ext.get_p_other(),
            "true_class": c,
        }
        data_list.append(data)

        id_ += 1

    print("None counter: {0}".format(none_counter))

    try:
        final_df = pd.DataFrame(data_list)
        final_df.to_pickle(save_path)
        print("Feature extraction successful!")
    except Exception as e:
        print(
            "Feature extraction failed to save results! Error: {0}".format(
                str(e)
            )
        )
