import sys
from os.path import dirname, abspath
import re
from functions import fetch, parse_url, create_folder, initiate_structure, edit_template, show_usage_guide, parse_credentials, parse_arguments

from urllib.parse import urlparse

if __name__ == "__main__":
    credentials_file = "\\".join([dirname(abspath(__file__)),"credentials.json"])

    args = parse_arguments(credentials_file)

    # Input
    Link = args.link

    # Parse platform from 
    Platform = str((urlparse(Link).netloc.split(".")[-2:])[0]).capitalize()

    # Disallowed Characters for Folder names
    Disallowed_Characters = r'[\\/*?:"<>|]'

    # Given the URL as Input parse it and return the info required for the request
    url, ID = parse_url(Platform,Link)

    # Make API call and fetch response
    response_json = fetch("{}{}".format(url,ID))

    # Fetch info from Response
    Challenge_Name = re.sub(Disallowed_Characters,"",  response_json['name'])
    Challenge_URL = str("\\".join([response_json['url'],"python"])).strip()
    Challenge_Rank = str(re.sub(' ','-', response_json['rank']['name'])).strip()
    Template_Path = "\\".join([dirname(abspath(__file__)),"Template.md"])
    Challenge_Tags = ', '.join(response_json['tags']).strip()

    # Path to try create the new challenge folder
    path = "\\".join([dirname(abspath(__file__)),Platform,Challenge_Rank,Challenge_Name])

    # Try to create a folder for this new challenge based on the full path.
    create_folder(path)

    # Initiate the Folder Structure - Create the files
    initiate_structure(path)

    README_path = "\\".join([dirname(abspath(__file__)),Platform,Challenge_Rank,Challenge_Name,"README.md"])

    # Model README.md based on Template.md
    edit_template(challenge_name=Challenge_Name,challenge_url=Challenge_URL,completion_date="Wednesday, 30 December 2024",tags=Challenge_Tags,template_path=Template_Path,readme_file=README_path)

    # Open Folder