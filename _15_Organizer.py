# import os

# def change_name(name, i):
#     new_name = name.replace(".", "")
#     # new_name = name.replace(f" ", f"_")
#     return new_name

# list_py = os.listdir("D:\Not For Public\\0xCybri-313\Bloggers Brackets\\bzot\\assets\images\product-images")
        
# for i, name in enumerate(list_py, start = 1):
#     if name.endswith(".webp"):
#         new_name = name.rstrip(".webp")
#         new_name_2 = change_name(name, i)
#         new_name_3 = new_name_2 + ".webp"
#         os.rename(name, new_name_3)

import os

# 1. The folder path (using r"" for Windows backslashes)
folder_path = r"D:\Not For Public\0xCybri-313\Bloggers Brackets\bzot\assets\images\product-images"

# Check if path exists to avoid errors
if os.path.exists(folder_path):
    # Get all files
    files = os.listdir(folder_path)
    
    # Filter only for .webp files (or remove the 'if' to rename EVERYTHING)
    # We sort the list to ensure the order is deterministic (optional but recommended)
    files.sort() 

    count = 1
    for filename in files:
        # Check for webp extension
            # Get the file extension (e.g., .webp)
            _, extension = os.path.splitext(filename)
            
            # 2. Define the new name pattern
            new_name = f"image_shoes_{count}{extension}"
            
            # 3. Create full paths
            old_file_path = os.path.join(folder_path, filename)
            new_file_path = os.path.join(folder_path, new_name)
            
            # Rename
            # We check if the name is different to avoid errors if a file is already named correctly
            if old_file_path != new_file_path:
                try:
                    os.rename(old_file_path, new_file_path)
                    print(f"Renamed: {filename} -> {new_name}")
                except FileExistsError:
                    print(f"Skipped: {new_name} already exists.")
            
            count += 1
else:
    print("Error: Folder path not found.")