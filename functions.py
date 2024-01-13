from datetime import datetime
from datetime import timezone
import requests
import time
import re
from urllib.parse import urlparse
import os
import sys
from jinja2 import Template

def ordinal(n: int) -> str:
    """
    derive the ordinal numeral for a given number n
    """
    return f"{n:d}{'tsnrhtdd'[(n//10%10!=1)*(n%10<4)*n%10::4]}"

def translate_date(a_date):

    date1 = datetime.date(datetime.fromisoformat(a_date[:-1]).astimezone(timezone.utc))

    dayOrdinal = ordinal(date1.day)
    
    return date1.strftime(f'%A, {dayOrdinal.strip()} %B %Y')

def make_api_call(url):
    try:
        
        # Issue a Request 
        response = requests.get(url)

        # Fetch a Response
        return response.json()
    
    except:
    
        return None
    
def get_pages(User):

    codewars_user = "https://www.codewars.com/api/v1/users/{}/code-challenges/completed?page=0".format(User)

    response_json = make_api_call(codewars_user)
    
    # Return Number of Completed Challenge Pages
    return int(response_json['totalPages'])

def get_user_info(username,platform):
    challenge_data = {}
    user_data = {}
    
    match platform:

        case "Codewars":

            Pages = get_pages(User=username)
            # Completed = response_json['totalItems']

            for x in range(Pages):
                current_page =  "https://www.codewars.com/api/v1/users/{}/code-challenges/completed?page={}".format(username,x)

                response_json = make_api_call(current_page)
                
                for challenge in response_json['data']:
                    challenge_data[str(challenge['id']).strip()] = {'Name': str(challenge['name']).strip(), 'Completed at': translate_date(challenge['completedAt'].strip()), 'Additional Info': {}}
                       
                for each in challenge_data:
                    
                    challenge_info = "https://www.codewars.com/api/v1/code-challenges/{}".format(each)

                    time.sleep(2)
                    
                    parsed_info = make_api_call(challenge_info)
                    
                    challenge_data[each]['Additional Info'] = {'url':  str(parsed_info['url'] + '/python').strip(), 'rank': str(re.sub(' ','-',parsed_info['rank']['name']).strip()), 'tags' : parsed_info['tags']}

            user_data[username] = { 'Total Completed' : int(response_json['totalItems']), 'Statistics' : { "1-kyu" : len([k for k,v in challenge_data.items() if v['Additional Info']['rank'] == "1-kyu"]),
                                    "2-kyu" : len([k for k,v in challenge_data.items() if v['Additional Info']['rank'] == "2-kyu"]), 
                                    "3-kyu" : len([k for k,v in challenge_data.items() if v['Additional Info']['rank'] == "3-kyu"]), 
                                    "4-kyu" : len([k for k,v in challenge_data.items() if v['Additional Info']['rank'] == "4-kyu"]),
                                    "5-kyu" : len([k for k,v in challenge_data.items() if v['Additional Info']['rank'] == "5-kyu"]),
                                    "6-kyu" : len([k for k,v in challenge_data.items() if v['Additional Info']['rank'] == "6-kyu"]),
                                    "7-kyu" : len([k for k,v in challenge_data.items() if v['Additional Info']['rank'] == "7-kyu"]), 
                                    "8-kyu" : len([k for k,v in challenge_data.items() if v['Additional Info']['rank'] == "8-kyu"])
                                    },'Challenges' : challenge_data }
            
            return user_data


def parse_url(Platform: str, url: str) -> str:
    match Platform:
        case "Codewars":
            # The API endpoint
            return ["https://www.codewars.com/api/v1/code-challenges/", parse_challenge_id(url)]
        case "exercism":
            return ""
        case "hackerrank":
            return ""
        case "leetcode":
            return ""

def fetch(url):
    try:
        
        # Issue a Request 
        with requests.get(url) as response:

            # Check request was successful
            response.raise_for_status()

        if response.status_code == 200:

            # Successful Response
            return response.json()

        else:
            print(f"Unexpected status code: {response.status_code}")
            return None

    except requests.exceptions.RequestException as e:
        
        # Handle exceptions
        print(f"Error making the request: {e}")
        return None

# Given a folder path, creates a folder if none exists.
def create_folder(folder_path):

    if os.path.exists(folder_path):
            
            print(f"A challenge by this name, already exists in your database.")
            sys.exit()

    else:

        try:
            # Use os.makedirs to create the folder and its parent directories if they don't exist
            os.makedirs(folder_path, exist_ok=True)

            # Get the subfolders from the path
            subfolders = folder_path.split(os.path.sep)

            # Return the last three subfolders
            print(f"Categorized challenge under {subfolders[-3]}, identified as difficulty \"{subfolders[-2]}\" and named \"{subfolders[-1]}\".")
    
        except PermissionError:
            print(f"Permission error: Unable to create folder.")
        
        except OSError as e:
            print(f"Error creating folder: {e}")

def initiate_structure(folder_path):

    try:
        # Check if the folder exists
        if not os.path.exists(folder_path):
            print("Error, folder doesn't exist.")
            sys.exit()
            
        # Check if the folder is empty
        if not os.listdir(folder_path):

            # Create an empty solution.py file
            with open(os.path.join(folder_path, 'solution.py'), 'w'):
                pass

            # Create an empty README.md file
            with open(os.path.join(folder_path, 'README.md'), 'w'):
                pass

            # Create notes.txt file
            with open(os.path.join(folder_path, 'notes.txt'), 'w') as notes_file:
                notes_file.write("Write your notes and observations here.")
                notes_file.close()
            
        else:
            print("Folder is not empty.")
    
    except FileNotFoundError:
        print(f"Error: Folder not found at path {folder_path}")
    
    except PermissionError:
        print(f"Error: Permission denied for folder at path {folder_path}")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def is_valid_url(url):
    try:

        # Attempt to parse the URL
        parsed_url = urlparse(url)

        # Check if the URL has both a scheme and a network location (netloc)
        if parsed_url.scheme and parsed_url.netloc:
            return parsed_url
        else:
            raise ValueError("URL is missing either the scheme or netloc.")
    
    except ValueError as ve:
        print(f"ValueError: {ve}")
        return False
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False
    
def parse_challenge_id(url):
    
    valid_domains = ["codewars", "hackerrank", "exercism", "leetcode"]

    try:

        # Parse the URL
        parsed_url = is_valid_url(url)

        # Check if the URL is valid and the main domain matches one of the options
        if parsed_url.scheme and parsed_url.netloc and any(domain in parsed_url.netloc for domain in valid_domains):
            
            # If the domain is "codewars," extract the challenge ID
            if "codewars" in parsed_url.netloc:
            
                path_segments = parsed_url.path.split("/")
                challenge_id = path_segments[2] if len(path_segments) >= 3 else None
                return challenge_id
            
            else:
                print("URL is valid, but the domain is not 'codewars'.")
        else:
            print("Invalid URL or domain does not match the specified options.")
   
    except ValueError:
        print("Invalid URL format.")
   
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def edit_template(challenge_name, completion_date, tags, template_path, readme_file):

    try:

        # Check if both the template file and readme file exist
        if not os.path.exists(template_path):
            print(f"Error: Template file not found at path {template_path}")
            return

        if not os.path.exists(readme_file):
            print(f"Error: README file not found at path {readme_file}")
            return

        # Read the content of the template file
        with open(template_path, 'r') as template_file:
            template_content = template_file.read()

        # Replace variables in the template content
        template_content = template_content.replace('<a id="challenge_name" href=""></a>', f'<a id="challenge_name" href="">{challenge_name}</a>')
        template_content = template_content.replace('<i id="completion_date" align="center"></i>', f'<i id="completion_date" align="center">{completion_date}</i>')
        template_content = template_content.replace('<i id="tags" align="center"></i>', f'<i id="tags" align="center">{tags}</i>')

        # Write the modified content back to the README file
        with open(readme_file, 'w') as readme_file_content:
            readme_file_content.write(template_content)

        print("README file edited and overwritten successfully.")
    except FileNotFoundError:
        print(f"Error: File not found.")
    except PermissionError:
        print(f"Error: Permission denied.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
