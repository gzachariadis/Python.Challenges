import subprocess

with open("output.txt", "w+") as output:
	subprocess.call(["python", "./update.py", "gzachariadis", "Codewars"], stdout = output)
