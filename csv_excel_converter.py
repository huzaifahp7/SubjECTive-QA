import os
import pandas as pd

# Function to convert CSV files to XLSX and delete duplicate files
def convert_csv_to_xlsx(directory):
    # Loop through all files in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".csv"):
            # Read CSV file into a pandas DataFrame
            csv_path = os.path.join(directory, filename)
            df = pd.read_csv(csv_path)

            # Create an Excel file with the same name
            xlsx_filename = os.path.splitext(filename)[0] + ".xlsx"
            xlsx_path = os.path.join(directory, xlsx_filename)

            # Save DataFrame to Excel file
            df.to_excel(xlsx_path, index=False)

            # Delete the original CSV file
            os.remove(csv_path)

# Specify the directory containing CSV files
csv_directory = "/Users/hp/Desktop/SubjECTive-QA/manual_annotations"

# Call the function to convert and delete files
convert_csv_to_xlsx(csv_directory)
