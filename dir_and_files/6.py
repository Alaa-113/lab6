import string

file_names = []

for letter in string.ascii_uppercase:
    file_name = f"{letter}.txt"
    file_names.append(file_name)
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(f"This is file {file_name}\n")

print("Generated files:")
print(", ".join(file_names))