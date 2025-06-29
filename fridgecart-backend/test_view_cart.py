import requests

url = "http://localhost:5000/view-cart"

response = requests.get(url)

print("Status Code:", response.status_code)
print("Cart Contents:", response.json())
