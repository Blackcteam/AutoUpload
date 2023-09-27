import requests

def upload_file(cpanel_url, username, password, local_file_path, remote_file_path):
    # Create a session object to handle cookies
    session = requests.Session()

    # Step 1: Login to cPanel and get the necessary cookies
    login_url = f"{cpanel_url}/login/"
    login_data = {
        "user": username,
        "pass": password,
        "cookie": "1",  # Enable cookie-based authentication
    }
    login_response = session.post(login_url, data=login_data)

    # Step 2: Upload the file
    upload_url = f"{cpanel_url}/execute/Fileman/upload_files"
    files = {
        "file-0": open(local_file_path, "rb"),
    }
    upload_data = {
        "file-0": (None, ""),
        "dir": remote_file_path,
        "fileop": "upload",
        "dir_path": "",
        "file_charset": "utf-8",
    }
    upload_response = session.post(upload_url, data=upload_data, files=files)

    # Step 3: Logout from cPanel
    logout_url = f"{cpanel_url}/logout/"
    logout_response = session.get(logout_url)

    # Check if the upload was successful
    if upload_response.status_code == 200:
        print(f"File uploaded successfully to {remote_file_path}")
    else:
        print("File upload failed")

# Set the cPanel server and credentials
cpanel_url = "https://your_cpanel_url"
username = "your_username"
password = "your_password"

# Set the local and remote file paths
local_file_path = "/path/to/local/file.txt"
remote_file_path = "/path/to/remote/file.txt"

# Upload the file
upload_file(cpanel_url, username, password, local_file_path, remote_file_path)