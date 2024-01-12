from datetime import datetime
from datetime import timezone
import requests
import time
import re
from urllib.parse import urlparse
import os
import sys

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
            return ["https://www.codewars.com/api/v1/code-challenges/", urlparse(url).path.split('/')[-2]]
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


def create_folder(folder_path):

    try:
        # Use os.makedirs to create the folder and its parent directories if they don't exist
        os.makedirs(folder_path, exist_ok=True)

        if os.path.exists(folder_path):
            
            print(f"A challenge by this name, already exists in your database.")
            sys.exit()

        else:
            
            print(f"Folder '{folder_path}' created successfully.")
    
    except PermissionError:
        print(f"Permission error: Unable to create folder.")
    
    except OSError as e:
        print(f"Error creating folder: {e}")
