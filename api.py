from flask import Flask, jsonify, request
from flask_cors import CORS
import json
from difflib import get_close_matches
import os

app = Flask(__name__)
CORS(app)

def load_disease_advice():
    try:
        with open('medicine.json') as file:
            return json.load(file)
    except Exception as e:
        print(f"Failed to load disease advice data: {e}")
        return {}
    
def find_close_matches(input_str, data, cutoff=0.5, n=1):
    keys = list(data.keys())
    close_matches = get_close_matches(input_str, keys, n=n, cutoff=cutoff)
    matches_info = [(match, data[match]) for match in close_matches]
    return matches_info

@app.route('/medicine', methods=['POST'])
def detect_medicine():
    data = request.json
    
    if 'medicine' in data:
        input_med = data['medicine']
        disease_info = load_disease_advice()
        matched_info = find_close_matches(input_med, disease_info)
        if matched_info:
            response_data = {
                "matches": [
                    {"Medicine Name": match, "Potential Uses": info['Uses'], "Possible Side Effects Include:": info['Side Effects']}
                    for match, info in matched_info
                ]
            }
            return jsonify(response_data), 200
        else:
            return jsonify({"message": "No matching information found."}), 404
    else:
        return jsonify({"error": "Missing 'medicine' key in the request."}), 400
    
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)