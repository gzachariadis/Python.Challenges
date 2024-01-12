import sys

import json

from functions import get_user_info

# Expected Inputs 

# - Username
# - Platform


## Given a username
## Return the number of completed challenges pages

def main():

    user_info = get_user_info(username=sys.argv[1],platform=sys.argv[2])

    print(json.dumps(user_info, sort_keys=False, indent=4)) 

    
if __name__ == "__main__":
    main()