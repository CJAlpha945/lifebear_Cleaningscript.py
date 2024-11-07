![image](https://github.com/user-attachments/assets/1e127100-64d2-4766-a818-02e86abd84a0)

# **Lifebear Data Processing**
This repository contains Python scripts for processing a CSV dataset named `lifebear.csv.csv`. The scripts include functionality for splitting the dataset into chunks, validating data, removing duplicates, and updating specific values. Here’s a breakdown of each code snippet to help you understand the workflow.

# **Table of Contents**
1. Project Overview
2. Prerequisites
3. Scripts and Functionality
  * Splitting the Dataset
  * Validating and Cleaning Data
  * Removing Duplicate Email Addresses
  * Replacing Gender Values
  * Combining Chunks
4. How to Run the Scripts
5. Notes
# **Project Overview**
This project involves processing a large CSV file in several steps:

* Splitting the dataset into smaller chunks for easier processing.
* Identifying and removing corrupt or invalid data.
* Removing duplicate email addresses.
* Updating gender values from numeric codes to text labels.
* Combining the modified chunks back into a single CSV file.
# **Prerequisites**
Make sure to have the following installed:

* Python (version 3.6 or higher)

* Pandas library

To install Pandas, run:
 <!-- Python block -->

```python
pip install pandas

```
# **Scripts and Functionality**

**Splitting the Dataset**

The first script splits the original CSV file into four equal-sized chunks and saves each chunk as a separate CSV file.
<!-- Python block -->

```python
import pandas as pd

# Define the number of chunks (4 equal parts)
num_chunks = 4

# Load the dataset
df = pd.read_csv("/content/lifebear.csv.csv", sep=';', low_memory=True)

# Determine the chunk size
chunk_size = len(df) // num_chunks

# Split the dataset into chunks and save them
for i in range(num_chunks):
    start_index = i * chunk_size
    end_index = (i + 1) * chunk_size if i < num_chunks - 1 else len(df)
    chunk = df.iloc[start_index:end_index]
    chunk.to_csv(f'/content/lifebear_dataset_chunk_{i+1}.csv', index=False)

print(f"The CSV file has been divided into {num_chunks} smaller portions.")

```
# Validating and Cleaning Data

This part of the code identifies and separates corrupt or invalid data based on specific conditions, such as incorrect date formats and invalid gender values.
<!-- Python block -->

```python
import pandas as pd
import re

# Functions to validate and check data
def is_invalid(value):
    return pd.isnull(value) or str(value).strip() == ''

def is_valid_created_at(value):
    pattern = r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$'
    return bool(re.match(pattern, str(value)))

def is_valid_birthday_on(value):
    pattern = r'^\d{4}-\d{2}-\d{2}$'
    return bool(re.match(pattern, str(value)))

def is_valid_gender(value):
    return value in [0, 1]

# Load the dataset and define columns to check
df = pd.read_csv("/content/lifebear.csv.csv", sep=';', low_memory=True)
columns_to_check = ['id', 'login_id', 'mail_address', 'password', 'created_at', 'salt', 'birthday_on', 'gender']

# Split and validate data, then save corrupt data separately
for i in range(4):
    ...
```
# Removing Duplicate Email Addresses

This script removes duplicate email addresses from a specified chunk and saves the duplicates to a separate file.
<!-- Python block -->

```python
import pandas as pd

try:
    df = pd.read_csv('/content/lifebear_dataset_chunk_4.csv')
    df_no_duplicates = df.drop_duplicates(subset=['mail_address'])
    
    # Save removed duplicates
    duplicate_emails = df[df.duplicated(subset=['mail_address'])]
    duplicate_emails.to_csv('duplicate_emails.csv', index=False)
    
    print(f"Removed {len(duplicate_emails)} duplicate email addresses.")
    ...
except FileNotFoundError:
    print("File not found.")
```
# Replacing Gender Values

This code replaces numeric gender values (0.0 and 1.0) with 'male' and 'female'.

<!-- Python block -->

```python
import pandas as pd

# Function to replace gender values
def replace_gender(chunk):
    chunk['gender'] = chunk['gender'].replace({0.0: 'male', 1.0: 'female'})
    return chunk

# Update each chunk and save
for file_path in chunk_files:
    df = pd.read_csv(file_path)
    df = replace_gender(df)
    df.to_csv(file_path, index=False)
    print(f"Updated {file_path} and saved.")

```
# Combining Chunks

Finally, this script combines all modified chunks into a single DataFrame and saves it as a new CSV file.
<!-- Python block -->

```python
import pandas as pd

# List of modified chunk file paths
chunk_files = [...]
chunks = [pd.read_csv(file_path) for file_path in chunk_files]

# Combine and save
combined_data = pd.concat(chunks)
combined_data.to_csv('/content/lifebear_dataset_combined.csv', index=False)

print("All chunks have been combined.")

```
# How to Run the Scripts
1. Clone the repository to your local machine.

2. Make sure all dependencies are installed.
 
3. Run each script sequentially, as described in the "Scripts and Functionality" section.
 
4. Check the output CSV files for cleaned and updated data.
# Notes

* Error Handling: Basic error handling is included to catch file-related errors.
  
* Data Validation: The scripts validate data formats for created_at, birthday_on, and gender.
  
* Memory Management: Using chunks helps manage memory when processing large datasets.
  
Feel free to contribute or suggest improvements!
