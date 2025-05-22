# Function to get Downloads directory
import os
from pathlib import Path

def get_downloads_directory():
    try:
        if os.name == 'nt':  # For Windows
            return str(Path(os.getenv("USERPROFILE")) / "Downloads")
        elif os.name == 'posix':  # For MacOS or Linux
            return str(Path.home() / "Downloads")
        else:
            raise Exception("Unsupported OS")
    except Exception as e:
        print(f"Error determining Downloads directory: {e}")
        raise
