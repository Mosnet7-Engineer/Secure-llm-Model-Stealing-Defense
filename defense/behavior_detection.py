from sklearn.ensemble import IsolationForest
import numpy as np

class BehaviorDetector:
    def __init__(self):
        self.model = IsolationForest(contamination=0.05)

    def fit(self, features):
        self.model.fit(features)

    def predict(self, features):
        return self.model.predict(features)

def extract_features(query_logs):
    features = []
    for q in query_logs:
        features.append([len(q), q.count("?")])
    return np.array(features)
