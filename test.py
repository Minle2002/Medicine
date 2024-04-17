import requests

url = "https://medicine-production-8a43.up.railway.app/medicine"

# Example JSON data
data = {
    "medicine": 'Acrotac 25mg Capsule'
}

response = requests.post(url, json=data)

print(response.json())