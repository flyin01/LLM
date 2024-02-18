# data reader module
import os
import numpy as np
import pandas as pd

### Define path of data

# Get the directory where this script is located
script_directory: str = os.getcwd()

# Define the relative path to the text file
relative_file_path: str = "trav/src/data/"

# Construct the absolute file path
absolute_file_path: str = os.path.join(script_directory, relative_file_path).replace("\\", "/")

### Read in one sample .txt file - Commented out!

# absolute_file_path = "C:/repo/LLM/trav/src/data/20230617_V75_1.txt"

# Sample file
sample_file_name: str = "20230617_V75_1.txt"

# Check path
print(absolute_file_path + sample_file_name)

# Initialize an empty list to store the file content
file_contents_list = []

# Read the file line by line and append each line to the list
with open(absolute_file_path + sample_file_name, "r", encoding="utf-8") as file:
    for line in file:
        file_contents_list.append(line.strip())  # Remove leading/trailing whitespace

# Check resulting list, txt file should be read in line by line.
for line_no, line in enumerate(file_contents_list[:12]):
    print(line_no, line)

for line_no, line in enumerate(file_contents_list[-12:]):
    print(line_no, line)

print(len(file_contents_list)) # Should match the rows of the .txt file


### Read in all .txt files

# initialize empty dict to store text corpus
file_contents_dict = {}

print(f"Absolute file path: {absolute_file_path}")

# iterate and read in each file in the folder
for filename in os.listdir(absolute_file_path):
    if filename.endswith(".txt"):
        file_path = os.path.join(absolute_file_path, filename)
        with open(file_path, "r", encoding="utf-8") as file:
            # read the entire file content as a string
            file_contents = file.readlines()
            # get the first sentence (header) and the rest of the content (corpus)
            first_sentence = file_contents[0].strip()
            corpus = ''.join(file_contents[1:]).strip()
            # add file name (without extension) as key and file content as value
            file_contents_dict[filename[:-4]] = {"File Name": filename[:-4], "File Header": first_sentence, "File Content": corpus}

# Check the resulting dictionary and check results
print(f"Number of dict entries: {len(file_contents_dict)}")

# Check structure and content 
for key, value in file_contents_dict.items():
    print(f"File Name: {value['File Name']}\nFile Header: {value['File Header']}\nFirst 100 characters of content: {value['File Content'][:100]}\n\n")

# Convert to pandas df
pdf = pd.DataFrame.from_dict(file_contents_dict, orient='index')
pdf.reset_index(inplace=True)
pdf = pdf.drop(columns=['index'])
pdf.columns = ["File Name", "File Header", "File Content"]
print(f"Shape of pdf: {pdf.shape}")
pdf.head()