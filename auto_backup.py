"""
Description:
  Program takes user provided file path(s) and automatically commits them to Github
  Program is intended to be used with Windows Task Scheduler to automatically commit changes to Github

Requirements:
  [x] Read .txt file to get file path(s) for local repo location(s)
  [x] File path location must already be a Github repo
  [x] Navigate to local repo(s)
  [x] Run: git add . | git commit -a --allow-empty-message -m "" | git push
  [x] Convert program into .exe for automatic running
  [x] Add program to Task Scheduler running every (x) days

Resources:
  https://stackoverflow.com/questions/11113896/use-git-commands-within-python-code
"""

import os, subprocess
import logging as log

# path to log file
log_path = '.\\log\\run.log'
# log_path = os.path.dirname(os.path.abspath(__file__)) + '\\log\\run.log'


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

# Runs relevant git commands
def git_run(path):
  # add changes for staging
  try:
    output = subprocess.run(
      ["git", "add", "."],
      cwd=path,
      check=True,
      capture_output=True,
      text=True
    ).stdout
    if output:
      log.info(output)
  except Exception as e:
    log.error(e)

  # commits repo changes
  try:
    output = subprocess.run(
      ["git", "commit", "-a", "--allow-empty-message", "-m", "\"\""],
      cwd=path,
      check=True,
      capture_output=True,
      text=True
    ).stdout
    if output:
      log.info(output)
  except Exception as e:
    log.error(e)

  # pushes changes to repo
  try:
    output = subprocess.run(
      ["git", "push"],
      cwd=path,
      check=True,
      capture_output=True,
      text=True
    ).stdout
    if output:
      log.info(output)
  except Exception as e:
    log.error(e)


# location being searched for path variables
path = "./paths/paths.txt"

# loops through paths provided to read each contained path
with open(path) as file:
  for line in file:

    # non-existant lines are being read. Not a major issue due to confirmation code.
    line = line.strip("\n").strip("\r")

    # confirms a line's path is valid
    if os.path.exists(line):
      # confirms the provided directory is a git repo
      if os.path.exists(line + "/.git"):
        log.info("Valid Directory, Valid Repository Found At: " + line)
        git_run(line)
      else:
        log.info("Valid Directory, No Repository Found At: " + line)
    else:
      log.info("Invalid Directory: " + line)

    log.info("\n\n")

file.close()
log.critical("Program Terminated")
