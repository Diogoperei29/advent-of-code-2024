# Advent of Code 2024

My personal solutions to the 2024 advent of code coding challenges, in python

Assumes .txt inputs.

Not all files are solutions, this is mostly a storage to all my attempts at finding the sollution!

Will organize one day (maybe)

## Input acquisition automation

The file 2024.py is an automation script that uses your session cookie to obtain the input files automatically, create a folder for the current day, download the input for an input.txt file and create a main.py that uses the example.py as a baseline and edits the necessary data for current day and year.

In the file you have to change the following:
- Add your session cookie (use inspect element on a browser and check storage)
- Add the HARDCODED_DAY ,if this variable is set to anything, that day will be used, otherwise the current day of the month is used.
