import sys
from os.path import dirname, abspath
import re
from functions import fetch, parse_url, create_folder
from urllib.parse import urlparse

Link = str(sys.argv[1])
Platform = str((urlparse(Link).netloc.split(".")[-2:])[0]).capitalize()

# Disallowed Characters for Folder names
Disallowed_Characters = r'[\\/*?:"<>|]'

# Given the URL as Input parse it and return the info required for the request
url, ID = parse_url(Platform,Link)

# Make API call and fetch response
response_json = fetch("{}{}".format(url,ID))

# Fetch info from Response
Challenge_Name = re.sub(Disallowed_Characters,"",  response_json['name'])
Challenge_URL = str(response_json['url']).strip()
Challenge_Rank = str(re.sub(' ','-', response_json['rank']['name'])).strip()

# Path to try create the new challenge folder
path = "\\".join([dirname(abspath(__file__)),Platform,Challenge_Rank,Challenge_Name])

# Try to create a folder for this new challenge based on the full path.
create_folder(path)

try:

    solution = open(path + '\{}'.format("solution.py") , 'w')
    solution.close()
    notes = open(path + '\{}'.format("notes.txt") , 'w')
    notes.close()
    readme = open(path + '\{}'.format("README.md") , 'w')
    readme.close()

except FileNotFoundError as e:
    print(f'An error occurred: {e}')
