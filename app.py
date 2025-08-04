from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load("kmeans_model.joblib")
scaler = joblib.load("scaler.joblib")
cluster_map = joblib.load("cluster_mapping.joblib")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = [float(x) for x in request.form.values()]
        scaled = scaler.transform([features])
        cluster = model.predict(scaled)[0]
        species = cluster_map.get(cluster, "Unknown")
        return render_template('index.html', prediction=f"Cluster: {cluster} → Species: {species}")
    except:
        return render_template('index.html', prediction="Error: Please enter valid numbers.")

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)
