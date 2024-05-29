import json
import random

# Load the JSON file
with open('testJson.json') as file:
    data = json.load(file)
    print(type(data))
# # Get a random key from the JSON data
# random_key = random.choice(list(data.keys()))

# # Print the corresponding value
# print(data[random_key])