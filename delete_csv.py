import os
import shutil

def keep_subdirectory_only(directory, subdirectory_name):
    # Get the list of all files and directories in the specified directory
    all_contents = os.listdir(directory)

    # Filter out the subdirectory you want to keep
    subdirectory_path = os.path.join(directory, subdirectory_name)
    contents_to_keep = [subdirectory_name]

    # Remove all files and directories except the subdirectory
    for item in all_contents:
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path) and item != subdirectory_name:
            shutil.rmtree(item_path)
        elif os.path.isfile(item_path) and item != subdirectory_name:
            os.remove(item_path)

    # Make the subdirectory the main directory
    os.chdir(subdirectory_path)

# Specify the directory path and the subdirectory to keep
main_directory = "/Users/hp/Desktop/SubjECTive-QA/manual_annotations"
subdirectory_to_keep = "/Users/hp/Desktop/SubjECTive-QA/manual_annotations/manual_annotations"

# Call the function to keep only the specified subdirectory
keep_subdirectory_only(main_directory, subdirectory_to_keep)
