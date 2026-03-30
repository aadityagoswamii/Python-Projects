import os
import shutil

# Folder path (change this to your folder)
folder_path = "test_folder"

# File type categories
file_types = {
    "Images": [".jpg", ".png", ".jpeg"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv"],
    "Python": [".py"]
}

# Loop through files
for file in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file)

    # Skip if it's a folder
    if os.path.isdir(file_path):
        continue

    # Get file extension
    _, extension = os.path.splitext(file)

    # Move file to correct folder
    for folder_name, extensions in file_types.items():
        if extension.lower() in extensions:
            target_folder = os.path.join(folder_path, folder_name)

            # Create folder if not exists
            if not os.path.exists(target_folder):
                os.makedirs(target_folder)

            shutil.move(file_path, os.path.join(target_folder, file))
            break

print("Files organized successfully!")