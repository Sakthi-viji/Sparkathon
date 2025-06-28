# fridge_detector.py

# MOCK VERSION: Returns dummy fridge items for testing
def detect_items(image_file):
    return ["milk", "eggs", "carrot"]

"""real api after sam ML API URL

import requests

def detect_items(image_file):
    url = 'http://localhost:5001/detect'  # Replace with actual ML API URL
    response = requests.post(url, files={'image': image_file})
    if response.status_code == 200:
        return response.json().get('items', [])
    else:
        return []"""
