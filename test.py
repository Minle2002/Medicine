import requests

url = "http://127.0.0.1:5000/medicine"

# Example JSON data
data = {
    "medicine": 'Acrotac 25mg Capsule'
}

response = requests.post(url, json=data)

print(response.json())