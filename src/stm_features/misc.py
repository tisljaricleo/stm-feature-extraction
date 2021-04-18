import stm_features.config as config
import matplotlib.pyplot as plt
import numpy as np
import pickle


def plot_heatmap(data, title: str, output="show", filename="image.png"):
    """
    Plots heatmap for all speed transitions.
    :param data: 2D numpy array.
    :param states_names: State names (x and y labels).
    :param title: Title for ploting.
    :param output:
    :param filename:
    :return:
    """
    states_names = config.SPEED_LIST
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.imshow(data, cmap="cividis", interpolation="none")
    ax.set_xticks(np.arange(len(states_names)))
    ax.set_yticks(np.arange(len(states_names)))
    ax.set_xticklabels(states_names)
    ax.set_yticklabels(states_names)
    plt.xlabel("Destination speed (%)")
    plt.ylabel("Origin speed (%)")
    ax.set_title(title)
    fig.tight_layout()
    if output == "show":
        plt.show()
    if output == "save":
        plt.savefig(filename, bbox_inches="tight")


def open_pickle(path: str):
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


def save_pickle(path: str, data):
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
