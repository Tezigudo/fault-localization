import json

# Read the input JSON file
with open('line_of_code-demo.json', 'r') as input_file:
    data = json.load(input_file)

# Create a new dictionary with the desired format
output_data = {file['path']: file['stats']['total'] for file in data['files']}

# Write the new dictionary to an output JSON file
with open('line_of_code-demo1.json', 'w') as output_file:
    json.dump(output_data, output_file, indent=4)

print("Conversion complete. Check the output.json file.")
