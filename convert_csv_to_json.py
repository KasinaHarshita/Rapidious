import csv
import json

csv_file = 'epi_r.csv'
json_file = 'epirecipes.json'

# Open CSV file with specified encoding
with open(csv_file, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

with open(json_file, 'w', encoding='utf-8') as f:
    json.dump(rows, f, indent=4)
