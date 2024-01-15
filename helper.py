import os
from os.path import abspath
from os.path import dirname

def get_immediate_subdirectories(a_dir):
	return [name for name in os.listdir(a_dir) if os.path.isdir(os.path.join(a_dir, name))]

def is_empty(path):
	try:
		if not does_path_exist(path):
			return False

		# Check if it's a file
		if os.path.isfile(path):
			return os.path.getsize(path) == 0

		# Check if it's a folder
		elif os.path.isdir(path):
			return not os.listdir(path)

		# Not a valid file or folder
		else:
			return False

	except Exception as e:
		print(f"An error occurred while checking if the path is empty: {e}")
		return False

def does_path_exist(path: str) -> bool:
	"""
    Check if the provided folder path is valid.

    Parameters:
    - folder_path (str): The path to the folder.

    Returns:
    - bool: True if the folder path is valid, False otherwise.
    """

	try:
		# Use os.path.normpath to normalize the path and handle potential issues
		normalized_path = os.path.normpath(path)

		# Check if the path exists
		if not os.path.exists(normalized_path):
			print(f"The path '{normalized_path}' does not exist.")
			return False

		# Path Valid
		return True

	except Exception as e:
		print(f"An error occurred while checking the folder path: {e}")
		return False

def create_file(folder_path: str, file_name: str, contents = "") -> bool:
	try:
		# Check if the Folder exists
		if not does_path_exist(folder_path):
			return False

		# Join the folder_path and filename
		file_path = os.path.join(folder_path, file_name)

		# Open the file in write mode to create an empty file
		with open(file_path, "w") as file:
			file.write(contents)

		return True

	except Exception as e:
		print(f"An error occurred while creating the file: {e}")
		return False

# Repository Directory
current_d = dirname(abspath(__file__))

# Platforms
Codewars = current_d + "\Codewars"
HackerRank = current_d + "\HackerRank"
Exercism = current_d + "\Exercism"
Leetcode = current_d + "\Leetcode"

# Platform Index Location
Codewars_README = os.path.normpath(Codewars + "\README.md")
HackerRank_README = os.path.normpath(HackerRank + "\README.md")
Exercism_README = os.path.normpath(Exercism + "\README.md")
Leetcode_README = os.path.normpath(Leetcode + "\README.md")

# Delete Every Platform Index before Reindexing
open(Codewars_README, "w").close()
open(HackerRank_README, "w").close()
open(Exercism_README, "w").close()
open(Leetcode_README, "w").close()

# Codewars

# for each difficulty level
for x in get_immediate_subdirectories(os.path.normpath(Codewars)):
	# Each difficulty README
	Difficulty_README = os.path.normpath(Codewars + "\\" + x + "\\README.md")

	# Each difficulty's challenges
	challenges = get_immediate_subdirectories(os.path.normpath(Codewars + "\\" + x))

	with open(Codewars_README, "a", encoding = "utf-8") as f:
		f.write("\n")
		f.write("## " + str(x))
		f.write("\n")
		f.write("\n")
		f.close()

	for y in challenges:
		with open(Codewars_README, "a", encoding = "utf-8") as f:
			f.write("\n")
			f.write(
					"- [" + str(y) + "](https://github.com/gzachariadis/Python.Challenges/tree/main/Codewars/" + x + "/" +
					str(y).replace(" ", "%20") + ")"
					)
			f.write("\n")
		f.close()

		with open(Difficulty_README, "a", encoding = "utf-8") as ff:
			ff.write("\n")
			ff.write(
					"- [" + str(y) + "](https://github.com/gzachariadis/Python.Challenges/tree/main/Codewars/" + x + "/" +
					str(y).replace(" ", "%20") + ")"
					)
			ff.write("\n")
		ff.close()

# Add invididual Indexes for Each Level
# Everything should be in Alphabetical Order

# Use Remove first and last character from string under 8-kyu as a Template for every other file.
# Find a way to create a template folder with README.md template and an empty python file each time I want to submit a new challenge.
