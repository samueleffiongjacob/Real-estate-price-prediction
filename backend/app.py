# backend/app.py
from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from config import Config
from flasgger import Swagger
import pickle
import numpy as np
from model.preprocess import preprocess_input

app = Flask(__name__)
app.config.from_object(Config)

# Initialize MySQL
mysql = MySQL(app)

# Swagger Config
swagger = Swagger(app)

# Load model
with open('model/model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    """
    Predict Real Estate Price
    ---
    parameters:
      - name: location
        in: formData
        type: string
        required: true
      - name: square_footage
        in: formData
        type: number
        required: true
      - name: bedrooms
        in: formData
        type: integer
        required: true
    responses:
      200:
        description: Predicted price
    """
    data = request.form
    input_data = preprocess_input(data)
    prediction = model.predict(np.array([input_data]))
    return jsonify({"predicted_price": prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)
