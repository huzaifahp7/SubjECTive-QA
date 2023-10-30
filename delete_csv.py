import os

# Directory containing CSV files
csv_directory = "manual_annotations"

# List all files in the directory
file_list = os.listdir(csv_directory)

# Filter and remove CSV files
for file_name in file_list:
    if file_name.endswith(".csv"):
        file_path = os.path.join(csv_directory, file_name)
        os.remove(file_path)
        print(f"Removed: {file_name}")

print("CSV files removed from the directory.")
