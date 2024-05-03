import csv
import json

medicine_data = {}

with open('medicine.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        medicine = row['Medicine Name'].lower()  # Convert to lowercase
        text = row['Uses']
        response = row['Side_effects']

        side_effects = [effect.strip() for effect in response.split(',')]

        if medicine not in medicine_data:
            medicine_data[medicine] = {'Uses': [], 'Side Effects': []}

        medicine_data[medicine]['Uses'].append(text)
        medicine_data[medicine]['Side Effects'].extend(side_effects)

for medicine in medicine_data.values():
    medicine['Uses'] = ', '.join(set(medicine['Uses']))

for medicine in medicine_data.values():
    medicine['Side Effects'] = list(set(medicine['Side Effects']))

with open('medicine.json', 'w') as jsonfile:
    json.dump(medicine_data, jsonfile, indent=4)