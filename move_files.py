import os

while True:

    while True:
        source_path = input("Please enter souce directory: ")
        try:
            source_folder_files = os.listdir(source_path)
            break
        except FileNotFoundError:
            print("Source directory not found!")

    while True:
        destination_path = input("Please enter destination directory: ")
        try:
            destination_folder_files = os.listdir(destination_path)
            break
        except FileNotFoundError:
            print("Destination directory not found!")

    while True:
        str_extensions = input("Enter extensions (separate entries by comma): ")
        extensions = tuple(str_extensions.split(", "))
        try:
            source_folder_files = [f for f in source_folder_files if f.endswith(extensions)]
            destination_folder_files = [f for f in destination_folder_files if f.endswith(extensions)]
            break
        except FileNotFoundError:
            print("Invalid extension(s)!")

    pending_files = 0

    for file in source_folder_files:
        if file not in destination_folder_files:
            pending_files += 1

    print("="*60)
    print("Source: " + source_path)
    print("Destination: " + destination_path)
    print(f"Extensions: {extensions}")
    print(f"Files to be moved: {pending_files}")
    print("="*60)
    confirmation = input("Does this look correct [Y/N]: ")

    if confirmation.upper() == "Y":
        break

for file in source_folder_files:
    if file not in destination_folder_files:
        source = source_path + file
        destination = destination_path + file

        os.rename(source, destination)
    
print(f"{pending_files} files successfully moved!")