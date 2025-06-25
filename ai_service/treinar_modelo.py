from sklearn.ensemble import IsolationForest
import numpy as np
import joblib

X = np.random.rand(100, 4)  # Dados fictícios para treinar
model = IsolationForest()
model.fit(X)
joblib.dump(model, "model.pkl")
