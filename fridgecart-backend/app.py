# app.py

from flask import Flask, request, jsonify
from fridge_detector import detect_items
from mock_data import item_to_product

app = Flask(__name__)
cart = []

@app.route('/')
def home():
    return "FridgeCart Backend is running."

@app.route('/upload-photo', methods=['POST'])
def upload_photo():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400
    image = request.files['image']
    items = detect_items(image)
    return jsonify({'items': items})

@app.route('/confirm-cart', methods=['POST'])
def confirm_cart():
    data = request.get_json()
    selected_items = data.get('items', [])
    global cart
    cart = [item_to_product.get(i, f"{i} (Unavailable)") for i in selected_items]
    return jsonify({'cart': cart})

@app.route('/view-cart', methods=['GET'])
def view_cart():
    return jsonify({'cart': cart})

if __name__ == '__main__':
    app.run(port=5000, debug=True)
