import requests
import sys
from os.path import dirname, abspath
import os
import re

# Required Inputs

# - Challenge ID 
# - Platform
# - Username

Disallowed_Characters = r'[\\/*?:"<>|]'

# The API endpoint
codewars_url = "https://www.codewars.com/api/v1/code-challenges/" + sys.argv[1]

# A GET request to the API
response = requests.get(codewars_url)

# Print the response
response_json = response.json()

Challenge_Name = re.sub(Disallowed_Characters,"",  response_json['name'])
Challenge_URL = str(response_json['url']).strip()
Challenge_Rank = str(re.sub(' ','-', response_json['rank']['name'])).strip()

# Repository Directory
current_d = dirname(abspath(__file__))
Platform = sys.argv[2]

full_path = current_d + '\{}'.format(Platform) + '\{}'.format(Challenge_Rank) + '\{}'.format(Challenge_Name)

if not os.path.exists(full_path):
    os.makedirs(full_path)

    try:

        solution = open(full_path + '\{}'.format("solution.py") , 'w')
        solution.close()
        notes = open(full_path + '\{}'.format("notes.txt") , 'w')
        notes.close()
        readme = open(full_path + '\{}'.format("README.md") , 'w')
        readme.close()

        print("New entry was added Successfully.")
    except FileNotFoundError as e:
        print(f'An error occurred: {e}')


else:
    print("Challenge Exists Already.")


