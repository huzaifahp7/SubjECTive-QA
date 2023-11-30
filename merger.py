import os
import shutil

# Set the paths for source directories and the destination directory
source_directories = ['/Users/hp/Desktop/SubjECTive-QA/Abhishek-annotations', '/Users/hp/Desktop/SubjECTive-QA/Rohan-annotations', '/Users/hp/Desktop/SubjECTive-QA/Andrew-annotations', '/Users/hp/Desktop/SubjECTive-QA/Veer-annotations', '/Users/hp/Desktop/SubjECTive-QA/Siddhant-annotations', '/Users/hp/Desktop/SubjECTive-QA/Huzaifa-annotations', '/Users/hp/Desktop/SubjECTive-QA/Dhruv-annotations', '/Users/hp/Desktop/SubjECTive-QA/Tarun-annotations', '/Users/hp/Desktop/SubjECTive-QA/Chandrashekaran-annotations']
destination_directory = '/Users/hp/Desktop/SubjECTive-QA/all_annotated'

# Initialize a counter for file names
counter = 0

# Dictionary to track encountered file names
encountered_files = {}

# Iterate through each source directory
for source_dir in source_directories:
    # Iterate through each file in the source directory
    for filename in os.listdir(source_dir):
            
            # Check if the file name has been encountered before
            if filename not in encountered_files:
                encountered_files[filename] = 1
            else:
                encountered_files[filename] += 1

            # Construct the new file name with the counter
            new_filename = f"{filename[:-5]}_{encountered_files[filename]}.xlsx"

            # Create the source file path
            source_file_path = os.path.join(source_dir, filename)

            # Create the destination file path
            destination_file_path = os.path.join(destination_directory, new_filename)

            # Copy the file to the destination directory
            shutil.copy(source_file_path, destination_file_path)

print("Files copied successfully.")
