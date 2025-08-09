"""
Description:
  Program takes user provided file path(s) and automatically commits them to Github
  Program is intended to be used with Windows Task Scheduler to automatically commit changes to Github

Requirements:
  [x] Read .txt file to get file path(s) for local repo location(s)
  [x] File path location must already be a Github repo
  [] Navigate to local repo(s)
  [] Run: git add . | git commit -a --allow-empty-message -m "" | git push

Resources:
  https://stackoverflow.com/questions/11113896/use-git-commands-within-python-code
"""

import os
import logging as log

log_path = os.path.dirname(os.path.abspath(__file__)) + '\\log\\run.log'

log.basicConfig(
    filename= log_path,
    level=log.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
# log.debug("debug message")
# log.info("info message")
# log.warning("warning message")
# log.error("error message")
# log.critical("critical message")

#############################################################################################################
#############################################################################################################
#############################################################################################################


log.critical("### ### ### V Program Starts V ### ### ###")

path = "./paths/paths.txt"

with open(path) as file:
  for line in file:

    # non-existant lines are being read. Not a major issue due to confirmation code.
    line = line.strip("\n").strip("\r")

    if os.path.exists(line):
      if os.path.exists(line + "/.git"):
        print("valid path")
        print(line + "/.git")
        log.info("Valid Directory, Valid Repository Found At: " + line)
      else:
        log.info("Valid Directory, No Repository Found At: " + line)
    else:
      log.info("Invalid Directory: " + line)

file.close()
log.critical("Program Terminated")
