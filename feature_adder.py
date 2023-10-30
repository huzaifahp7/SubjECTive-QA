import os
import pandas as pd
import chardet

# List of features
features = ["Clear", "Assertive", "Cautious", "Optimistic", "Specific", "Relevant"]

def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
    return result['encoding']

def add_empty_columns(file_path, features):
    try:
        encoding = detect_encoding(file_path)
        if file_path.endswith(".csv"):
            df = pd.read_csv(file_path, encoding=encoding)
        elif file_path.endswith(".xlsx"):
            df = pd.read_excel(file_path, engine='openpyxl')
        else:
            print(f"Unsupported file format for {file_path}")
            return

        for feature in features:
            df[feature] = None

        return df
    except Exception as e:
        print(f"Error processing {file_path}: {str(e)}")
        return None
def main():
    dir_path = "datasets"
    directory_path = "manual_annotations"

    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

    for filename in os.listdir(dir_path):
        file_path = os.path.join(dir_path, filename)
        new_file_path = os.path.join(directory_path, filename)

        modified_df = add_empty_columns(file_path, features)

        if modified_df is not None:
            if filename.endswith(".csv"):
                modified_df.to_csv(new_file_path, index=False)
            elif filename.endswith(".xlsx"):
                modified_df.to_excel(new_file_path, index=False)

if __name__ == "__main__":
    main()

        
