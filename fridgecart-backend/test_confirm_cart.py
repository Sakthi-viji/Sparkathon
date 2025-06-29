import requests

url = "http://localhost:5000/confirm-cart"

payload = {
    "items": ["milk", "eggs", "carrot"]  # simulate selected items from detection
}

response = requests.post(url, json=payload)

print("Status Code:", response.status_code)
print("Response:", response.json())
