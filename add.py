import requests
import sys
import json

# Required Inputs

# - Challenge ID 
# - Platform
# - Username


# The API endpoint
codewars_url = "https://www.codewars.com/api/v1/code-challenges/" + sys.argv[1]

# A GET request to the API
response = requests.get(codewars_url)

# Print the response
response_json = response.json()

Challenge_Name = response_json['name']
Challenge_URL = response_json['url']
Challenge_Rank = response_json['rank']['name']



print(Challenge_Name)
print(Challenge_URL)
print(Challenge_Rank)
