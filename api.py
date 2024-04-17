import json
from difflib import get_close_matches

def load_disease_advice():
    try:
        with open('medicine.json') as file:
            return json.load(file)
    except Exception as e:
        print(f"Failed to load disease advice data: {e}")
        return {}
    
def find_close_matches(input_str, data, cutoff=0.5, n=10):
    keys = list(data.keys())
    close_matches = get_close_matches(input_str, keys, n=n, cutoff=cutoff)
    matches_info = [(match, data[match]) for match in close_matches]
    return matches_info

input_med = "Halosys -S Ointment"
disease_info = load_disease_advice()
matched_info = find_close_matches(input_med, disease_info)

if matched_info:
    print("Close matches found:")
    for match, info in matched_info:
        print(f"Medicine: {match}")
        print("Information:")
        print(info)
        print()
else:
    print("No matching information found.")