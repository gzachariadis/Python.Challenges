from os.path import dirname, abspath
import os 

def get_immediate_subdirectories(a_dir):
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]


# Repository Directory

current_d = dirname(abspath(__file__))

# Platforms
Codewars = current_d + '\Codewars'
HackerRank = current_d + '\HackerRank'
Exercism = current_d + '\Exercism'
Leetcode = current_d + '\Leetcode'

# Platform Index Location
Codewars_README = os.path.normpath(Codewars + '\README.md')
HackerRank_README = os.path.normpath(HackerRank + '\README.md')
Exercism_README = os.path.normpath(Exercism + '\README.md')
Leetcode_README = os.path.normpath(Leetcode + '\README.md')

# Delete Every Platform Index before Reindexing
open(Codewars_README, 'w').close()
open(HackerRank_README, 'w').close()
open(Exercism_README, 'w').close()
open(Leetcode_README, 'w').close()

# Codewars

# for each difficulty level
for x in get_immediate_subdirectories(os.path.normpath(Codewars)):

    # Each difficulty README
    Difficulty_README = os.path.normpath(Codewars + '\\' + x + '\\README.md')

    # Each difficulty's challenges
    challenges = get_immediate_subdirectories(os.path.normpath(Codewars + '\\' + x))
    
    with open(Codewars_README, "a", encoding="utf-8") as f:
        f.write("\n")
        f.write("## " + str(x))
        f.write("\n")
        f.write("\n")
        f.close()

    for y in challenges:
        with open(Codewars_README, "a", encoding="utf-8") as f:
            f.write("\n")
            f.write("- [" + str(y) + "](https://github.com/gzachariadis/Python.Challenges/tree/main/Codewars/" + x + '/' + str(y).replace(' ', '%20') + ')')
            f.write("\n")
        f.close()

        with open(Difficulty_README, "a", encoding="utf-8") as ff:
            ff.write("\n")
            ff.write("- [" + str(y) + "](https://github.com/gzachariadis/Python.Challenges/tree/main/Codewars/" + x + '/' + str(y).replace(' ', '%20') + ')')
            ff.write("\n")
        ff.close()


# Add invididual Indexes for Each Level
# Everything should be in Alphabetical Order

# Use Remove first and last character from string under 8-kyu as a Template for every other file.
# Find a way to create a template folder with README.md template and an empty python file each time I want to submit a new challenge.

        