import re
from os.path import abspath, dirname
from urllib.parse import urlparse

from functions import (create_folder, edit_template, extract_id, fetch,
                       initiate_structure, is_valid_url, parse_arguments)

# Disallowed Characters for Folder names
Disallowed_Characters = r'[\\/*?:"<>|]'

if __name__ == "__main__":
  # Part 1 - Validate Data

  # Read Credentials
  credentials_file = "\\".join(
      [dirname(abspath(__file__)), "credentials.json"])

  # Verify Credentials file valid

  # Parse Arguments
  args = parse_arguments(credentials_file)

  # Validation

  # Step 1: Verify provided link is a valid URL
  if is_valid_url(args.link):

    # Step 2 : Verify link domain is one of the permitted options.

    Platform = str(
        (urlparse(args.link).netloc.split(".")[-2:])[0]).capitalize()

  # Step 3 : Check Valid Username

  # Step 4 : Check Template.md file exists.

  # Step 5: Check Template.md file contains appropriate ids.

  # Part 2 - Request Info

  # Given the URL extract the Challenge ID
  ID = extract_id(args.link)

  # Make API call and Fetch Response
  response_json = fetch("{}{}".format(args.link, ID))

  # Determine info based on Request Response
  Challenge_Name = re.sub(Disallowed_Characters, "", response_json["name"])
  Challenge_URL = str("\\".join([response_json["url"], "python"])).strip()
  Challenge_Rank = str(re.sub(" ", "-", response_json["rank"]["name"])).strip()
  Challenge_Tags = ", ".join(response_json["tags"]).strip()

  # Call update.py

  # Fetch response in the form of database.json

  # Validate

  # Parse JSON

  # Fetch Completion Date

  # Part 3 - Update Structure

  # Determine New Challenge file path
  path = "\\".join(
      [dirname(abspath(__file__)), Platform, Challenge_Rank, Challenge_Name])

  # Determine template path based on argument or keep default value.
  Template_Path = "\\".join([dirname(abspath(__file__)), "Template.md"])

  # Create a folder for this new challenge based on path.
  create_folder(path)

  # Initiate the Folder Structure
  initiate_structure(path)

  # Model README.md based on Template
  edit_template(
      challenge_name=Challenge_Name,
      challenge_url=Challenge_URL,
      completion_date="Wednesday, 30 December 2024",
      tags=Challenge_Tags,
      template_path=Template_Path,
      readme_file="\\".join([path, "README.md"]),
  )

  # Part 4 - Results

  # Ask user for their solution?

  # Open Folder?

  # open_file
