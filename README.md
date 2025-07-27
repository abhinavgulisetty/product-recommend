# product-recommend

This project demonstrates a minimal recommendation system built with **TensorFlow**, served through a **Flask** web application, and visualized using **D3.js**.

## Features

- Sample ratings data and a small TensorFlow model for collaborative filtering.
- Flask endpoints to request recommendations for a given user ID.
- D3.js visualization of the predicted ratings.

## Setup

1. Install dependencies (preferably in a virtual environment):
   ```bash
   pip install -r requirements.txt
   ```
2. Train the recommendation model:
   ```bash
   python model/model.py
   ```
   This saves `model/recommender.h5`.
3. Run the Flask app:
   ```bash
   python app.py
   ```
4. Visit `http://localhost:5000` in your browser and enter a user ID to see recommendations rendered in a bar chart.

The included dataset and model are intentionally small for demonstration purposes. Feel free to adapt the architecture and data to fit real-world scenarios.
