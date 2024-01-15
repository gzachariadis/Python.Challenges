import argparse
import json
import os
import re
import sys
import time
from datetime import datetime
from datetime import timezone
from urllib.parse import urlparse

import requests

from helper import create_file
from helper import does_path_exist
from helper import is_empty

def show_usage_guide():
	print("Usage: python add.py [options]")
	print("Options:")
	print("  -h, --help         Show this help message and exit")
	print("  -l, --link         Specify the challenge link/url (required)")
	print("  -u, --username     Specify your username (defaults to credentials file)")
	print("  -t, --template     Specify Template (defaults to 'Template.md')")
	print("\n")
	exit()

def parse_arguments(credentials_file):
	try:
		parser = argparse.ArgumentParser(description = "Automating the process of adding new challenges to the database.")

		parser.add_argument("-l", "--link", type = str, help = "Specify the challenge link/url", required = True,)
		parser.add_argument(
				"-u", "--username", type = str, default = parse_credentials(credentials_file), help = "Specify your username",
				)
		parser.add_argument("-t", "--template", type = str, default = "Template.md", help = "Specify the output directory",)

		args = parser.parse_args()

		return args

	except:
		show_usage_guide()

def parse_credentials(file_path):
	try:
		with open(file_path, "r") as file:
			json_data = json.load(file)
			return (json_data.get("User", {}).get("Codewars", {}).get("username", None))
	except (FileNotFoundError, json.JSONDecodeError):
		return None

def ordinal(n: int) -> str:
	"""
    derive the ordinal numeral for a given number n
    """
	return f"{n:d}{'tsnrhtdd'[(n//10 % 10 != 1)*(n % 10 < 4)*n % 10::4]}"

def translate_date(a_date):
	date1 = datetime.date(datetime.fromisoformat(a_date[:-1]).astimezone(timezone.utc))

	dayOrdinal = ordinal(date1.day)

	return date1.strftime(f"%A, {dayOrdinal.strip()} %B %Y")

def make_api_call(url):
	try:
		# Issue a Request
		response = requests.get(url)

		# Fetch a Response
		return response.json()

	except:
		return None

def pages(User: str) -> int:
	codewars_user = "https://www.codewars.com/api/v1/users/{}/code-challenges/completed?page=0".format(User)

	response_json = make_api_call(codewars_user)

	# Return Number of Completed Challenge Pages
	return response_json["totalPages"]

def get_user_info(username, platform):
	challenge_data = {}
	user_data = {}

	match platform:
		case "Codewars":
			Pages = pages(User = username)
			# Completed = response_json['totalItems']

			for x in range(Pages):
				current_page = "https://www.codewars.com/api/v1/users/{}/code-challenges/completed?page={}".format(username, x)

				response_json = make_api_call(current_page)

				for challenge in response_json["data"]:
					challenge_data[str(challenge["id"]).strip()] = {
							"Name": str(challenge["name"]).strip(),
							"Completed at": translate_date(challenge["completedAt"].strip()),
							"Additional Info": {},
							}

				for each in challenge_data:
					challenge_info = "https://www.codewars.com/api/v1/code-challenges/{}".format(each)

					time.sleep(2)

					parsed_info = make_api_call(challenge_info)

					challenge_data[each]["Additional Info"] = {
							"url": str(parsed_info["url"] + "/python").strip(),
							"rank": str(re.sub(" ", "-", parsed_info["rank"]["name"]).strip()),
							"tags": parsed_info["tags"],
							}

			user_data[username] = {
					"Total Completed": int(response_json["totalItems"]),
					"Statistics": {
							"1-kyu": len([k for k, v in challenge_data.items() if v["Additional Info"]["rank"] == "1-kyu"]),
							"2-kyu": len([k for k, v in challenge_data.items() if v["Additional Info"]["rank"] == "2-kyu"]),
							"3-kyu": len([k for k, v in challenge_data.items() if v["Additional Info"]["rank"] == "3-kyu"]),
							"4-kyu": len([k for k, v in challenge_data.items() if v["Additional Info"]["rank"] == "4-kyu"]),
							"5-kyu": len([k for k, v in challenge_data.items() if v["Additional Info"]["rank"] == "5-kyu"]),
							"6-kyu": len([k for k, v in challenge_data.items() if v["Additional Info"]["rank"] == "6-kyu"]),
							"7-kyu": len([k for k, v in challenge_data.items() if v["Additional Info"]["rank"] == "7-kyu"]),
							"8-kyu": len([k for k, v in challenge_data.items() if v["Additional Info"]["rank"] == "8-kyu"]),
							},
					"Challenges": challenge_data,
					}

			return user_data

def parse_url(Platform: str, url: str) -> str:
	match Platform:
		case "Codewars":
			# The API endpoint
			return ["https://www.codewars.com/api/v1/code-challenges/", extract_id(url),]
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
	if does_path_exist(folder_path):
		print(f"A challenge by this name, already exists in your database.")
		sys.exit()

	else:
		try:
			# Use os.makedirs to create the folder and its parent directories if they don't exist
			os.makedirs(folder_path, exist_ok = True)

			# Get the subfolders from the path
			subfolders = folder_path.split(os.path.sep)

			# Return the last three subfolders
			#   print(f"Categorized challenge under {
			#   subfolders[-3]}, identified as difficulty \"{subfolders[-2]}\" and named \"{subfolders[-1]}\".")

		except PermissionError:
			print(f"Permission error: Unable to create folder.")

		except OSError as e:
			print(f"Error creating folder: {e}")

def initiate_structure(folder_path):
	try:
		# Check if the folder exists
		if not does_path_exist(folder_path):
			# TODO: What is should do here?
			pass

		# Check if the folder is empty
		if is_empty(folder_path):
			# Create an empty solution.py file
			create_file(folder_path, file_name = "solution.py")

			# Create an empty README.md file
			create_file(folder_path = folder_path, file_name = "README.md")

			# Create a notes.txt file
			create_file(
					folder_path = folder_path, file_name = "notes.txt", contents = "Write your notes and observations here.",
					)

		else:
			pass
			#! TODO: Folder is not empty, what should it be done about that?

	except FileNotFoundError:
		print(f"Error: Folder not found at path {folder_path}")

	except PermissionError:
		print(f"Error: Permission denied for folder at path {folder_path}")

	except Exception as e:
		print(f"An unexpected error occurred: {e}")

def is_valid_url(url):
	try:
		result = urlparse(url)

		# Check if the URL has both a scheme and a network location (netloc)
		if result.scheme and result.netloc:
			return all([result.scheme, result.netloc])

	except ValueError as ve:
		print(f"ValueError: {ve}")
		return False

	except Exception as e:
		print(f"An unexpected error occurred: {e}")
		return False

def extract_id(url):
	valid_domains = ["codewars", "hackerrank", "exercism", "leetcode"]

	try:
		# Check if the URL is valid and the main domain matches one of the options
		if (url.scheme and url.netloc and any(domain in url.netloc for domain in valid_domains)):
			# If the domain is "codewars," extract the challenge ID
			if "codewars" in url.netloc:
				path_segments = url.path.split("/")
				challenge_id = (path_segments[2] if len(path_segments) >= 3 else None)
				return challenge_id

			else:
				print("URL is valid, but the domain is not 'codewars'.")
		else:
			print("Invalid URL or domain does not match the specified options.")

	except ValueError:
		print("Invalid URL format.")

	except Exception as e:
		print(f"An unexpected error occurred: {e}")

def edit_template(challenge_name, challenge_url, completion_date, tags, template_path, readme_file,):
	try:
		print("Modelling Challenge README.md after provided Template file...")

		# Check if both the template file and readme file exist
		if not os.path.exists(template_path):
			print(f"Error: Template file not found at path {template_path}")
			return

		if not os.path.exists(readme_file):
			print(f"Error: README file not found at path {readme_file}")
			return

		# Read the content of the template file
		with open(template_path, "r") as template_file:
			template_content = template_file.read()

		# Replace variables in the template content
		template_content = template_content.replace(
				'<a id="challenge_name" href=""></a>', f'<a id="challenge_name" href="{challenge_url}">{challenge_name}</a>',
				)
		template_content = template_content.replace(
				'<i id="completion_date" align="center"></i>', f'<i id="completion_date" align="center">{completion_date}</i>',
				)
		template_content = template_content.replace(
				'<i id="tags" align="center"></i>', f'<i id="tags" align="center">{tags}</i>',
				)

		# Write the modified content back to the README file
		with open(readme_file, "w") as readme_file_content:
			readme_file_content.write(template_content)

		print("README.md file edited and overwritten successfully.")

	except FileNotFoundError:
		print(f"Error: File not found.")
	except PermissionError:
		print(f"Error: Permission denied.")
	except Exception as e:
		print(f"An unexpected error occurred: {e}")
