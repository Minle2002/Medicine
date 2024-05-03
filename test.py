import requests

url = "https://medicine-production-8a43.up.railway.app/medicine"

data = {
    "medicine": 'allegra'
}

response = requests.post(url, json=data)

print(response.json())