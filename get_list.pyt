import dropbox
from dropbox.exceptions import AuthError

# Dropbox API credentials
ACCESS_TOKEN = 'sl.ByqO84KWlVa1F7WtJUPzAZQPmbtcy07MXYnfGPrD6RVyiXMYacccKjysfj8gZ5b4rbjUW0_rQppk3uq7NByxGrLeFsuIvP0T9k1iLu_T9qqxGDpoNrAWFtv2hEM0g2GlrpSHdPVFCt1z8cOelaji5e8'

# Initialize Dropbox client
dbx = dropbox.Dropbox(ACCESS_TOKEN)

# Function to list files in a folder
def list_files(folder_path):
    try:
        # Call list_folder method to get metadata of files in the folder
        files = dbx.files_list_folder(folder_path)
        # Iterate through each file and print its name
        for entry in files.entries:
            print(entry.name)
    except AuthError as e:
        print("Authentication error:", e)

# Usage example: List files in the root folder
list_files('')
