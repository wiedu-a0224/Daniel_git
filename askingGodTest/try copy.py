import json
import random

# Load the JSON file
file = 'E:/Daniel_git/askingGodTest/stickPoetry.json'
with open(file, 'r', encoding='utf-8') as df:
    data = json.load(df)
    # print(type(data))
# Get a random key from the JSON data
random_data = random.choice(data)
# print(random_data)
# Print the corresponding value 
values_1 = random_data.get('stick_poetry')
print(values_1)
values_2 = random_data.get('stick_9')
print(values_2)