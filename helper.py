from os.path import dirname, abspath
import os 

def get_immediate_subdirectories(a_dir):
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]

current_d = dirname(abspath(__file__))
Codewars = current_d + '\Codewars'
Codewars_README = os.path.normpath(Codewars + '\README.md')

open(Codewars_README, 'w').close()

for x in get_immediate_subdirectories(os.path.normpath(Codewars)):
    challenges = get_immediate_subdirectories(os.path.normpath(Codewars + '\\' + x))

    with open(Codewars_README, "a", encoding="utf-8") as f:
        f.write("\n")
        f.write("## " + str(x))
        f.write("\n")
        f.write("\n")
        f.close()

    for y in challenges:
        with open(Codewars_README, "a", encoding="utf-8") as f:
            f.write("- " + str(y))
            f.write("\n")
        f.close()

# Add Links to Folders for Each Challenges
# Test spaces between the Challenges
# Add invididual Indexes for Each Level
# Everything should be in Alphabetical Order

# Use Remove first and last character from string under 8-kyu as a Template for every other file.
# Find a way to create a template folder with README.md template and an empty python file each time I want to submit a new challenge.
# Add a To-do Road Map to the README.md
        