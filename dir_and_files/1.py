import os

def list_directories(path):
    directories = []
    for item in os.listdir(path):
        if os.path.isdir(os.path.join(path, item)):
            directories.append(item)
    return directories

def list_files(path):
    files = []
    for item in os.listdir(path):
        if os.path.isfile(os.path.join(path, item)):
            files.append(item)
    return files

def list_all(path):
    all_items = []
    for item in os.listdir(path):
        all_items.append(item)
    return all_items

path = input("Enter the directory path (leave blank for current directory): ").strip()

if not path:
    path = os.getcwd()
else:
    path = os.path.expanduser(path)
    path = os.path.abspath(path)
    path = os.path.normpath(path)

if os.path.exists(path):
    print("\nDirectories:")
    print(list_directories(path))

    print("\nFiles:")
    print(list_files(path))

    print("\nAll items (Directories & Files):")
    print(list_all(path))
else:
    print("Invalid path! Please enter a valid directory path.")
