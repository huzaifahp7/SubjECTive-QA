import os
import pandas as pd

# List of features
features = ["Clear", "Assertive", "Cautious", "Optimistic", "Specific", "Relevant"]

dir_path1 = "datasets"

directory_path = "manual_annotations"

# Iterate through transcript files and add empty columns
for filename in os.listdir(dir_path1):
    if filename.endswith(".csv"):  # Assuming the transcripts are in CSV format
        file_path = os.path.join(directory_path, filename)
        df = pd.read_csv(file_path)

        # Add empty columns for each feature
        for feature in features:
            df[feature] = None

        # Save the modified DataFrame back to the file
        df.to_csv(file_path, index=False)
        
    if filename.endswith(".xlsx"):
        file_path = os.path.join(directory_path, filename)
        df = pd.read_excel(file_path)

        # Add empty columns for each feature
        for feature in features:
            df[feature] = None

        # Save the modified DataFrame back to the file
        df.to_excel(file_path, index=False)
        
