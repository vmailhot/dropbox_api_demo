import dropbox
from dropbox.exceptions import AuthError

# Dropbox API credentials
ACCESS_TOKEN = 'sl.ByqO84KWlVa1F7WtJUPzAZQPmbtcy07MXYnfGPrD6RVyiXMYacccKjysfj8gZ5b4rbjUW0_rQppk3uq7NByxGrLeFsuIvP0T9k1iLu_T9qqxGDpoNrAWFtv2hEM0g2GlrpSHdPVFCt1z8cOelaji5e8'

# Initialize Dropbox client
dbx = dropbox.Dropbox(ACCESS_TOKEN)

# Function to download a file from Dropbox
def download_file(dropbox_path, local_path):
    try:
        # Call files_download_to_file to download the file from Dropbox to local_path
        dbx.files_download_to_file(local_path, dropbox_path)
        print("File downloaded successfully.")
    except AuthError as e:
        print("Authentication error:", e)

# Usage example: Download a file named 'example.txt' from Dropbox root folder to local 'downloads' folder
dropbox_file_path = '/test_upload.txt'
local_file_path = 'downloads\\test_download.txt'
download_file(dropbox_file_path, local_file_path)
