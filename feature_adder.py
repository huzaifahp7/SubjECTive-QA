import os
import pandas as pd

# List of features
features = ["Clarity", "Coherence", "Aggression", "Optimism", "Specificity", "Relevance"]

# Path to the 'cleaned_transcripts' directory
directory_path = "cleaned_transcripts"

# Iterate through transcript files and add empty columns
for filename in os.listdir(directory_path):
    if filename.endswith(".csv"):  # Assuming the transcripts are in CSV format
        file_path = os.path.join(directory_path, filename)
        df = pd.read_csv(file_path)

        # Add empty columns for each feature
        for feature in features:
            df[feature] = None

        # Save the modified DataFrame back to the file
        df.to_csv(file_path, index=False)
