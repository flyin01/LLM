# data reader module
import os
import numpy as np
import pandas as pd

### Read in one sample text file 

# absolute_file_path = "C:/repo/LLM/trav/src/data/20230617_V75_1.txt"

# Get the directory where this script is located
script_directory: str = os.getcwd()

# Define the relative path to the text file
relative_file_path: str = "trav/src/data/"

# Construct the absolute file path
absolute_file_path: str = os.path.join(script_directory, relative_file_path).replace("\\", "/")

# Sample file
sample_file_name: str = "20230617_V75_1.txt"

# Initialize an empty list to store the file contents
file_contents_list = []

# Read the file line by line and append each line to the list
with open(absolute_file_path + sample_file_name, "r", encoding="utf-8") as file:
    for line in file:
        file_contents_list.append(line.strip())  # Remove leading/trailing whitespace

# Check resulting list
print(file_contents_list[0:4])



### Read in all files

# initialize empty dict to store text corpus
file_contents_dict = {}

print(f"Absolute file path: {absolute_file_path}")

# iterate and read in each file in the folder
for filename in os.listdir(absolute_file_path):
    if filename.endswith(".txt"):
        file_path = os.path.join(absolute_file_path, filename)
        with open(absolute_file_path, "r", encoding="utf-8") as file:
            # read the entire file content as a string
            file_contents = file.read()
            # add the file name (withouth extension) as key
            # and the file conent as the value
            file_contents_dict[filename[:-4]] = file_contents

# print the resulting dictionary
for filename,content in file_contents_dict.items():
    print(f"File: {filename}, Content: {content[:50]}...")

print(file_contents_dict)

