import os
import shutil
from datetime import datetime

# Path to your Downloads directory
script_dir = os.path.dirname(os.path.abspath(__file__))
downloads_dir = os.path.join(script_dir, "Downloads")

# List all files in the Downloads directory
files = os.listdir(downloads_dir)

# Iterate over each file in the Downloads folder
for file in files:
    file_path = os.path.join(downloads_dir, file) 

    if os.path.isdir(file_path):
        continue

    # Get the modification time of the file
    modified_time = os.path.getmtime(file_path)

    # Convert the modification time to a datetime object
    date = datetime.fromtimestamp(modified_time)
    year = date.year
    month = date.strftime("%B")

    # Print each file and their modification dates (for testing purposes)
    print(f"File: {file}, Modified: {month} {year}")

    # Create the directory path for the year and month
    folder_path = os.path.join(downloads_dir, str(year), month)

    # Create the directory if it doesn't exist
    os.makedirs(folder_path, exist_ok=True)

    # Move the file to the new directory
    new_file_path = os.path.join(folder_path, file)
    shutil.move(file_path, new_file_path)

    # Print a confirmation message
    print(f"Moved {file} to {folder_path}")


# Please be careful to follow instructions on how to run the program; review Step 3.
# The Run menu or right-click > Run do not work in the simulated environment. You must use the terminal window as directed.
    
