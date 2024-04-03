import dropbox
from dropbox.exceptions import AuthError, ApiError

# Dropbox API credentials
APP_KEY = 'c1cy6wsfq51brqy'
APP_SECRET = 'rb2dysuosh85zjs'
ACCESS_TOKEN = 'sl.ByqO84KWlVa1F7WtJUPzAZQPmbtcy07MXYnfGPrD6RVyiXMYacccKjysfj8gZ5b4rbjUW0_rQppk3uq7NByxGrLeFsuIvP0T9k1iLu_T9qqxGDpoNrAWFtv2hEM0g2GlrpSHdPVFCt1z8cOelaji5e8'

# Initialize Dropbox client
dbx = dropbox.Dropbox(ACCESS_TOKEN)

# Function to upload a file to Dropbox
def upload_file(file_path, dropbox_path):
    try:
        with open(file_path, 'rb') as f:
            dbx.files_upload(f.read(), dropbox_path)
        print("File uploaded successfully.")
    except AuthError as e:
        print("Authentication error:", e)
    except ApiError as e:
        print("API error:", e)

# Usage example
# Using double backslashes
file_path = 'test_dropbox\\test_upload.txt'

# Using a raw string
#file_path = r'test_dropbox\test_upload.txt'

dropbox_path = '/test_upload.txt'
upload_file(file_path, dropbox_path)
