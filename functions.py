from datetime import datetime
from datetime import timezone
import requests
import time
import re

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
        