import sys

import json

from functions import get_user_info

# Expected Inputs 

# - Username
# - Platform

def main():

    # Create a a dictionary with all the required user info
    user_info = get_user_info(username=sys.argv[1],platform=sys.argv[2])

    print(json.dumps(user_info, sort_keys=False, indent=4)) 

    # Count how many folders immediate subfolder each kyu level has

    # if Statistics kyu != kyu-Folders 
        # compare Folders with user_info challenge names
        # return result
    
    # for each in result
        # create a Folder with kyu challenge name
        # create within this folder
            # solution.py - empty file
            # notes.txt - empty file
            # README.md - based on Template
            # Ask user to submit their solution?
    
if __name__ == "__main__":
    main()