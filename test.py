import requests

url = "http://127.0.0.1:5000/medicine"

data = {
    "medicine": 'allegra'
}

response = requests.post(url, json=data)

print(response.json())