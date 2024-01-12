import requests
import sys
import time

import json
import re

from functions import translate_date

# Expected Inputs 

# - Username
# - platform

def make_api_call(url):
    try:

        response = requests.get(url)

        # Fetch a Response
        return response.json()
    
    except:
        return None
    
## Given a username
## Return the number of completed challenges pages
def get_pages(User):

    codewars_user = "https://www.codewars.com/api/v1/users/{}/code-challenges/completed?page=0".format(User)

    response_json = make_api_call(codewars_user)
    # Return Number of Pages
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

            user_data[username] = { 'Completed' : int(response_json['totalItems']), 'Challenges' : challenge_data }
            
            return user_data

# 
def main():
    user_info = get_user_info(username=sys.argv[1],platform=sys.argv[2])

    print(json.dumps(user_info, sort_keys=False, indent=4)) 

if __name__ == "__main__":
    main()