source_file = input("Enter the source file path: ").strip()
destination_file = input("Enter the destination file path: ").strip()

try:
    with open(source_file, "r", encoding="utf-8") as src, open(destination_file, "w", encoding="utf-8") as dest:
        dest.write(src.read())
    print("File copied.")
except FileNotFoundError:
    print("Source file not found.")
except Exception as e:
    print("An error occurred:", e)
