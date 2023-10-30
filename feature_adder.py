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


        
