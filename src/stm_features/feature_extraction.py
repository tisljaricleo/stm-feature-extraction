import numpy as np


class FeatureExtraction(object):
    def __init__(self, stm):
        self.stm = stm
        self.stm_orig = stm
        self.total_sum = np.sum(stm)
        self.filter_stm()

    def filter_stm(self):
        """Filters STM"""
        max_val = 0.2 * np.max(self.stm)  # Remove 20% of maximal value.
        self.stm = np.where(self.stm < max_val, 0, self.stm)
        self.stm = self.stm / np.sum(self.stm)

    def get_mass_center(self):
        """Computes the center of mas of the STM

        Returns:
            (int, int): Center of mass (x, y)
        """
        # marginal distributions
        dx = np.sum(self.stm, 1)
        dy = np.sum(self.stm, 0)
        # expected values
        X, Y = self.stm.shape
        cx = np.sum(dx * np.arange(X))
        cy = np.sum(dy * np.arange(Y))
        return int(cx), int(cy)

    def get_p_area(self):
        """Gets the percentage of area coverage
        Counts all chells that have value larger then 0, then divides it
        with total area (20x20=400)

        Returns:
            (float): Percentage of covered area (0-1)
        """
        data = self.stm[np.where(self.stm > 0)]
        return round(len(data) / float(400), 2)

    def get_p_break(self):
        return round(np.sum(self.stm_orig[13:19, 0:6]) / self.total_sum, 2)

    def get_p_acceleration(self):
        return round(np.sum(self.stm_orig[0:6, 13:19]) / self.total_sum, 2)

    def get_p_congestion(self):
        return round(np.sum(self.stm_orig[0:6, 0:6]) / self.total_sum, 2)

    def get_p_unstable(self):
        return round(np.sum(self.stm_orig[7:12, 7:12]) / self.total_sum, 2)

    def get_p_freeflow(self):
        return round(np.sum(self.stm_orig[13:19, 13:19]) / self.total_sum, 2)

    def get_p_other(self):
        sumator = (
            np.sum(self.stm_orig[7:12, 0:6])
            + np.sum(self.stm_orig[0:6, 7:12])
            + np.sum(self.stm_orig[13:19, 7:12])
            + np.sum(self.stm_orig[7:12, 13:19])
        )
        return round(sumator / self.total_sum, 2)

    def get_true_class(self):
        congestion = self.get_p_congestion()
        unstable = self.get_p_unstable()
        freeflow = self.get_p_freeflow()

        class_ = 0
        if congestion > unstable and congestion > freeflow:
            class_ = 0
        elif unstable > congestion and unstable > freeflow:
            class_ = 1
        elif freeflow > congestion and freeflow > unstable:
            class_ = 2
        else:
            None

        return class_
