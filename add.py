from os.path import dirname, abspath
from functions import fetch, parse_url, create_folder, initiate_structure, edit_template, show_usage_guide, parse_credentials, parse_arguments

from urllib.parse import urlparse
import re

# Disallowed Characters for Folder names
Disallowed_Characters = r'[\\/*?:"<>|]'

if __name__ == "__main__":
    
    credentials_file = "\\".join([dirname(abspath(__file__)),"credentials.json"])

    args = parse_arguments(credentials_file)

    # Link based on Script Arguments
    Link = args.link

    # Verify link is valid
    # Verify link domain is one of the permitted options.
    Platform = str((urlparse(Link).netloc.split(".")[-2:])[0]).capitalize()

    # Determine template path based on argument or keep default value.
    Template_Path = "\\".join([dirname(abspath(__file__)),"Template.md"])
    
    # Determine Challenge name
    Challenge_Name = re.sub(Disallowed_Characters,"",  response_json['name'])

    # Given the URL as Input parse it and return the info required for the request
    url, ID = parse_url(Platform,Link)

    # Make API call and Fetch Response
    response_json = fetch("{}{}".format(url,ID))

    # Determine info
    Challenge_URL = str("\\".join([response_json['url'],"python"])).strip()
    Challenge_Rank = str(re.sub(' ','-', response_json['rank']['name'])).strip()
    Challenge_Tags = ', '.join(response_json['tags']).strip()

    # Determine New Challenge file path
    path = "\\".join([dirname(abspath(__file__)),Platform,Challenge_Rank,Challenge_Name])

    # Create a folder for this new challenge based on path.
    create_folder(path)

    # Initiate the Folder Structure
    initiate_structure(path)

    # Model README.md based on Template
    edit_template(challenge_name=Challenge_Name,challenge_url=Challenge_URL,completion_date="Wednesday, 30 December 2024",tags=Challenge_Tags,template_path=Template_Path,readme_file="\\".join(path,"README.md"]))

    # Ask user for their solution?
    
    # Open Folder?
    open_file
