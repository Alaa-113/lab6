import os

file_path = input("Enter the file path to delete: ").strip()

if os.path.exists(file_path):
    if os.access(file_path, os.W_OK):
        try:
            os.remove(file_path)
            print("File deleted.")
        except Exception as e:
            print("An error occurred:", e)
    else:
        print("Permission denied: You do not have write access to this file.")
else:
    print("File not found")
