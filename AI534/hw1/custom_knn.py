import numpy as np
from collections import defaultdict


class KNNClassifier:
    def __init__(self, k):
        self.k = k
        self.points = []
        self.labels = []

    def fit(self, x_train, y_train):
        self.points = np.array(x_train)
        self.labels = np.array(y_train)

    def predict(self, new_points, order=2):
        res = []
        feature_map = defaultdict(int)
        for new_point in new_points:
            distances = np.linalg.norm(self.points - new_point, ord=order, axis=1)
            k_min_indices = np.argpartition(distances, self.k)[:self.k]

            for idx in k_min_indices:
                feature_map[tuple(self.labels[idx])] += 1
            res.append(max(feature_map.items(), key=lambda x: x[1])[0])
            feature_map.clear()
        return np.array(res)