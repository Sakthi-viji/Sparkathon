import requests

url = "http://localhost:5000/upload-photo"  # your Flask backend

with open("sample_fridge.jpg", "rb") as img:
    files = {'image': img}
    response = requests.post(url, files=files)

print("Status Code:", response.status_code)
print("Response JSON:", response.json())
