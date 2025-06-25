from flask import Flask, request, jsonify
import joblib
import numpy as np
import os

app = Flask(__name__)
MODEL_PATH = "model.pkl"

if os.path.exists(MODEL_PATH):
    model = joblib.load(MODEL_PATH)
else:
    model = None

@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({"error": "Modelo não carregado"}), 500
    data = request.get_json()
    features = np.array(data['features']).reshape(1, -1)
    prediction = model.predict(features)
    return jsonify({"prediction": prediction[0]}), 200

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "Servidor rodando"}), 200
@app.route('/metrics', methods=['GET'])
def metrics():
    return """
# HELP dummy_metric Métrica de teste
# TYPE dummy_metric gauge
dummy_metric 1
""", 200, {'Content-Type': 'text/plain; charset=utf-8'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
