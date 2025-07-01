from flask import Flask, request, jsonify, render_template
from fridge_detector import detect_items
from mock_data import get_mock_products, get_recipes

app = Flask(__name__)

# Set scanpage.html as homepage
@app.route('/')
def home():
    return render_template('scanpage.html')

@app.route('/recipes.html')
def recipes():
    return render_template('recipes.html')

@app.route('/fridge.html')
def fridge():
    return render_template('fridge.html')

@app.route('/myfridge.html')
def myfridge():
    return render_template('myfridge.html')

@app.route('/cart.html')
def cart():
    return render_template('cart.html')

@app.route('/checkout.html')
def checkout():
    return render_template('checkout.html')

# API: Detect items from uploaded image
@app.route('/api/detect', methods=['POST'])
def detect():
    image = request.files['image']
    items = detect_items(image)
    return jsonify({'items': items})

# API: Return current fridge items
@app.route('/api/fridge', methods=['GET'])
def fridge_items():
    items = ['banana', 'apple', 'oats']
    return jsonify({'items': items})

# API: Return mock cart products
@app.route('/api/cart', methods=['GET'])
def get_cart():
    return jsonify({'cart': get_mock_products()})

# API: Return recipes
@app.route('/api/recipes', methods=['GET'])
def recipe_list():
    return jsonify({'recipes': get_recipes()})

if __name__ == '__main__':
    app.run(debug=True)
