import os
import pandas as pd

# Directory containing CSV files
csv_directory = "manual_annotations"

# Directory where you want to save the Excel files
excel_directory = "manual_annotations"

# Create the Excel directory if it doesn't exist
if not os.path.exists(excel_directory):
    os.makedirs(excel_directory)

# List all CSV files in the CSV directory
csv_files = [f for f in os.listdir(csv_directory) if f.endswith(".csv")]

# Loop through each CSV file, read it, and save it as an Excel file
for csv_file in csv_files:
    csv_path = os.path.join(csv_directory, csv_file)
    excel_file = os.path.splitext(csv_file)[0] + ".xlsx"  # Change the file extension to .xlsx

    # Read the CSV file
    df = pd.read_csv(csv_path)

    # Create the path for the Excel file in the Excel directory
    excel_path = os.path.join(excel_directory, excel_file)

    # Save the DataFrame as an Excel file
    df.to_excel(excel_path, index=False, engine='openpyxl')

print("Conversion of CSV to Excel files complete.")
