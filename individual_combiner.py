import os
import pandas as pd

base_directory = "/Users/hp/Desktop/SubjECTive-QA/all_annotated"
output_directory = "individual_datasets"
os.makedirs(output_directory, exist_ok=True)

attribute_columns = ['CLEAR', 'ASSERTIVE', 'CAUTIOUS', 'OPTIMISTIC', 'SPECIFIC', 'RELEVANT']

# Initialize an empty DataFrame to store the final result
final_df = pd.DataFrame()

# Iterate through files and create individual datasets
for file in os.listdir(base_directory):
    if os.path.isfile(os.path.join(base_directory, file)):
        # Extracting company name, quarter, and year from the file name
        ticker, quarter, year, _ = file.split('_')

        # Reading the file and creating a DataFrame
        df = pd.read_excel(os.path.join(base_directory, file))

        # Convert column titles to uppercase
        df.columns = df.columns.str.upper()

        # Adding company details as columns in the DataFrame
        df['COMPANYNAME'] = ticker
        df['QUARTER'] = quarter
        df['YEAR'] = year

        # Combine the current file with the existing final_df
        final_df = pd.concat([final_df, df])

# Calculate the mode for each combination of 'QUESTION' and 'ANSWER' within each group
grouped_df = final_df.groupby(['COMPANYNAME', 'QUARTER', 'YEAR', 'ASKER', 'RESPONDER', 'QUESTION', 'ANSWER'])[attribute_columns].apply(
    lambda x: x.mode().iloc[0] if not x.mode().empty else '1').reset_index()

# Merge the mode results with the final_df to get other details
result_df = pd.merge(grouped_df, final_df[['COMPANYNAME', 'QUARTER', 'YEAR', 'QUESTION', 'ANSWER']], on=['COMPANYNAME', 'QUARTER', 'YEAR', 'QUESTION', 'ANSWER'])

# Reordering columns
col_order = ['COMPANYNAME', 'QUARTER', 'YEAR', 'ASKER', 'RESPONDER', 'QUESTION', 'ANSWER'] + attribute_columns

# Save the combined result to individual Excel files for each group
for group_name, group_data in result_df.groupby(['COMPANYNAME', 'QUARTER', 'YEAR']):
    output_file = os.path.join(output_directory, f"{group_name[0]}_{group_name[1]}_{group_name[2]}_combined_dataset.xlsx")
    group_data[col_order].to_excel(output_file, index=False)






