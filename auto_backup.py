"""
Description:
  Program takes user provided file path(s) and automatically commits them to Github
  Program is intended to be used with Windows Task Scheduler to automatically commit changes to Github

Requirements:
  [] Read .txt file to get file path(s) for local repo location(s)
  [] File path location must already be a Github repo
  [] Navigate to local repo(s)
  [] Run: git add . | git commit -a --allow-empty-message -m "" | git push

Resources:
  https://stackoverflow.com/questions/11113896/use-git-commands-within-python-code
"""

import os

with open("./paths/paths.txt") as file:
  for line in file:
    line = line.strip("\n")
    print(line)

file.close()

# path = os.path.dirname(os.path.abspath(__file__)) + '\\Log\\template.log'
