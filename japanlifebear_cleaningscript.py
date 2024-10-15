import pandas as pd

# Define the number of chunks (4 equal parts)
num_chunks = 4

# Load the dataset
df = pd.read_csv("/content/lifebear.csv.csv", sep=';', low_memory=True)

# Determine the chunk size based on the length of the dataset
chunk_size = len(df) // num_chunks

# Split the dataset into 4 chunks and save each chunk as a separate CSV file
for i in range(num_chunks):
    start_index = i * chunk_size
    end_index = (i + 1) * chunk_size if i < num_chunks - 1 else len(df)
    chunk = df.iloc[start_index:end_index]
    chunk.to_csv(f'/content/lifebear_dataset_chunk_{i+1}.csv', index=False)

print(f"The CSV file has been divided into {num_chunks} smaller portions.")
import pandas as pd
import re

# Function to check for invalid data (null or empty)
def is_invalid(value):
    return pd.isnull(value) or str(value).strip() == ''

# Function to validate if 'created_at' follows the correct format
def is_valid_created_at(value):
    pattern = r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$'  # Format: year-mm-dd hh:mm:ss
    return bool(re.match(pattern, str(value)))

# Function to validate if 'birthday_on' follows the correct format
def is_valid_birthday_on(value):
    pattern = r'^\d{4}-\d{2}-\d{2}$'  # Format: year-mm-dd
    return bool(re.match(pattern, str(value)))

# Function to validate if 'gender' is either 1 or 0
def is_valid_gender(value):
    return value in [0, 1]

# Load the dataset
df = pd.read_csv("/content/lifebear.csv.csv", sep=';', low_memory=True)

# Define the number of chunks (4 equal parts)
num_chunks = 4
chunk_size = len(df) // num_chunks

# List of columns to check for null/empty values
columns_to_check = ['id', 'login_id', 'mail_address', 'password', 'created_at', 'salt', 'birthday_on', 'gender']

# Process each chunk
for i in range(num_chunks):
    start_index = i * chunk_size
    end_index = (i + 1) * chunk_size if i < num_chunks - 1 else len(df)

    # Extract chunk
    chunk = df.iloc[start_index:end_index]

    # Create a mask to find invalid data
    invalid_data_mask = chunk[columns_to_check].applymap(is_invalid).any(axis=1)

    # Check for invalid 'created_at', 'birthday_on', and 'gender'
    invalid_created_at_mask = ~chunk['created_at'].apply(is_valid_created_at)
    invalid_birthday_on_mask = ~chunk['birthday_on'].apply(is_valid_birthday_on)
    invalid_gender_mask = ~chunk['gender'].apply(is_valid_gender)

    # Combine all invalid masks
    total_invalid_mask = invalid_data_mask | invalid_created_at_mask | invalid_birthday_on_mask | invalid_gender_mask

    # Separate corrupt data
    corrupt_data = chunk[total_invalid_mask]

    # Separate clean data
    clean_data = chunk[~total_invalid_mask]

    # Save corrupt data if any
    if not corrupt_data.empty:
        corrupt_data.to_csv(f'/content/corrupt_data_chunk_{i+1}.csv', index=False)
        print(f"Corrupt data found and saved to 'corrupt_data_chunk_{i+1}.csv'. Total rows: {len(corrupt_data)}")

    # Save the clean chunk data
    clean_data.to_csv(f'/content/lifebear_dataset_chunk_{i+1}.csv', index=False)

print(f"The CSV file has been divided into {num_chunks} smaller portions and corrupt data has been separated.")
