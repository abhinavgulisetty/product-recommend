import os
import json
import pandas as pd
from flask import Flask, request, render_template, jsonify
import tensorflow as tf

MODEL_PATH = os.path.join('model', 'recommender.h5')
DATA_PATH = os.path.join('data', 'ratings.csv')

app = Flask(__name__)

# Load data and model on startup
ratings = pd.read_csv(DATA_PATH)
num_users = ratings['user_id'].max() + 1
num_products = ratings['product_id'].max() + 1

if os.path.exists(MODEL_PATH):
    model = tf.keras.models.load_model(MODEL_PATH)
else:
    model = None


@app.route('/')
def index():
    return render_template('index.html', num_users=num_users-1)


@app.route('/recommend', methods=['POST'])
def recommend():
    user_id = int(request.form.get('user_id', 0))
    if model is None:
        # If no model, return static recommendations
        recommendations = [
            {'product_id': int(pid), 'rating': float(r)}
            for pid, r in enumerate([5, 4, 3])
        ]
    else:
        product_ids = list(range(num_products))
        user_array = [user_id] * num_products
        predictions = model.predict([user_array, product_ids], verbose=0).flatten()
        top_indices = predictions.argsort()[::-1][:5]
        recommendations = [
            {'product_id': int(pid), 'rating': float(predictions[pid])}
            for pid in top_indices
        ]
    return jsonify(recommendations)


if __name__ == '__main__':
    app.run(debug=True)
