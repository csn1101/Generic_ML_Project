import sys
import os

def add(a,b):
    c = a+b
    return c

def export_dataframe_to_csv(df, file_name):
    current_dir = os.getcwd()
    data_dir = os.path.join(current_dir, "data")
    os.makedirs(data_dir, exist_ok=True)
    file_path = os.path.join(data_dir, f"{file_name}.csv")
    df.to_csv(file_path, index=False)
    print(f"CSV file saved at: {file_path}")