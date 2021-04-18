import pandas as pd
import pickle


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


data = open_pickle(
    "/home/leo/git_repos/github/stm-feature-extraction/src/final_df.pkl"
)

print()