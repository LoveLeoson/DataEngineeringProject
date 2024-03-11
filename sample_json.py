import json
import random
with open('data.json', 'r') as file:
    data = json.load(file)

if isinstance(data, list):
    sample_size = max(1, len(data) // 10) 
    sampled_data = random.sample(data, sample_size)
else:
    raise TypeError("Unsupported JSON structure.")

with open('sampled_data.json', 'w') as outfile:
    json.dump(sampled_data, outfile, indent=4)
