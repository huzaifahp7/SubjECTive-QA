import os
import pandas as pd

input_directory = "individual_datasets"

# Iterate through files in individual_datasets
for file in os.listdir(input_directory):
    if os.path.isfile(os.path.join(input_directory, file)):
        # Read the file into a DataFrame
        df = pd.read_excel(os.path.join(input_directory, file))

        # Drop duplicate rows and modify the original DataFrame
        df.drop_duplicates(inplace=True)

        # Save the modified DataFrame back to the same file
        df.to_excel(os.path.join(input_directory, file), index=False)
