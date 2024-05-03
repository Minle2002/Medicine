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
    # Convert input string to lowercase
    input_str_lower = input_str.lower()
    
    # Convert keys in data dictionary to lowercase
    data_lower = {key.lower(): value for key, value in data.items()}
    
    keys = list(data_lower.keys())
    
    # Find close matches using lowercase input and keys
    close_matches = get_close_matches(input_str_lower, keys, n=n, cutoff=cutoff)
    
    # Retrieve original case matches and their corresponding values
    matches_info = [(original_case_key, data[original_case_key]) for original_case_key in close_matches]
    
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
                    {"medicine": match, "Uses": info['Uses'], "Side Effects:": info['Side Effects']}
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