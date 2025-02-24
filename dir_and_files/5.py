file_path = input("Enter the file path to save the list: ").strip()

data_list = []
print("Enter list items (type 'STOP' to finish):")

while True:
    item = input().strip()
    if item.upper() == "STOP":
        break
    data_list.append(item)

try:
    with open(file_path, 'w', encoding='utf-8') as file:
        for item in data_list:
            file.write(item + "\n")
    print("List has been written to the file successfully.")
except Exception as e:
    print("An error occurred:", e)
