import csv
import json

medicine_data = {}

# Read data from CSV file
with open('medicine.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        medicine = row['Medicine Name']
        text = row['Uses']
        response = row['Side_effects']

        # Split side effects into a list
        side_effects = [effect.strip() for effect in response.split(',')]

        # If medicine is not in dictionary, add it
        if medicine not in medicine_data:
            medicine_data[medicine] = {'Uses': [], 'Side Effects': []}

        # Append uses and side effects
        medicine_data[medicine]['Uses'].append(text)
        medicine_data[medicine]['Side Effects'].extend(side_effects)

# Convert uses to a comma-separated string
for medicine in medicine_data.values():
    medicine['Uses'] = ', '.join(set(medicine['Uses']))

# Remove duplicate side effects for each medicine
for medicine in medicine_data.values():
    medicine['Side Effects'] = list(set(medicine['Side Effects']))

# Write data to JSON file
with open('medicine.json', 'w') as jsonfile:
    json.dump(medicine_data, jsonfile, indent=4)