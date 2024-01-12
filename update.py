import requests
import sys

import re
from datetime import datetime
from datetime import timezone
import dateutil.parser

def ordinal(n: int) -> str:
    """
    derive the ordinal numeral for a given number n
    """
    return f"{n:d}{'tsnrhtdd'[(n//10%10!=1)*(n%10<4)*n%10::4]}"

def translate_date(a_date):

    date1 = datetime.date(datetime.fromisoformat(a_date[:-1]).astimezone(timezone.utc))

    dayOrdinal = ordinal(date1.day)
    
    return  date1.strftime(f'%A, {dayOrdinal.strip()} %B %Y')

# Expected Inputs 

# - Username

codewars_user = "https://www.codewars.com/api/v1/users/{}/code-challenges/completed?page=0".format(sys.argv[1])

# A GET request to the API
response = requests.get(codewars_user)

# Print the response
response_json = response.json()

Pages = response_json['totalPages']
Completed = response_json['totalItems']

data = {}
for x in response_json['data']:
    data[str(x['name']).strip()] = str(x['id']).strip(), translate_date(x['completedAt'].strip())


print(data)