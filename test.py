import requests

url = "http://127.0.0.1:5000/medicine"

data = {
    "medicine": 'Fiber'
}

response = requests.post(url, json=data)

print(response.json())