import os
import pandas as pd

base_directory = "/Users/hp/Desktop/SubjECTive-QA/all_annotated"
attribute_columns = ['CLEAR', 'ASSERTIVE', 'CAUTIOUS', 'OPTIMISTIC', 'SPECIFIC', 'RELEVANT']

# Step 1: Combine all files into one DataFrame
combined_dataframes = []

for file in os.listdir(base_directory):
    if os.path.isfile(os.path.join(base_directory, file)):
        # Extracting company name, quarter, and year from the file name
        ticker, quarter, year, number = file[:-5].split('_')

        # Reading the file and creating a DataFrame
        df = pd.read_excel(os.path.join(base_directory, file))

        # Convert column titles to uppercase
        df.columns = df.columns.str.upper()

        # Adding company details as columns in the DataFrame
        df['COMPANYNAME'] = ticker
        df['QUARTER'] = quarter
        df['YEAR'] = year

        # Adding the DataFrame to the list
        combined_dataframes.append(df)

# Combine all DataFrames into one DataFrame
combined_df = pd.concat(combined_dataframes, ignore_index=True)

# Step 2: Calculate the mode for each combination of 'QUESTION' and 'ANSWER'
mode_df = combined_df.groupby(['QUESTION', 'ANSWER'])[attribute_columns].apply(lambda x: x.mode().iloc[0] if not x.mode().empty else '1').reset_index()

# Step 3: Merge the mode results with the original DataFrame to get other details
result_df = pd.merge(mode_df, combined_df[['ASKER', 'RESPONDER', 'QUESTION', 'ANSWER', 'COMPANYNAME', 'QUARTER', 'YEAR']], on=['QUESTION', 'ANSWER'])

# Reordering columns
col_order = ['COMPANYNAME', 'QUARTER', 'YEAR', 'ASKER', 'RESPONDER','QUESTION', 'ANSWER'] + attribute_columns
result_df = result_df[col_order]

# Step 4: Drop duplicate rows to retain only one row for each unique 'QUESTION' and 'ANSWER' pair
result_df.drop_duplicates(subset=['QUESTION', 'ANSWER'], inplace=True)

# Step 5: Save to CSV
result_df.to_csv("final_dataset.csv", index=False)
result_df.to_excel("final_dataset.xlsx", index=False)
