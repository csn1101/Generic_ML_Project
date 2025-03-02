import sys
import os
import numpy as np 
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error

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

def evaluate_model(true,predicted):
    mae = mean_absolute_error(true,predicted)
    mse = mean_squared_error(true,predicted)
    r2 = r2_score(true,predicted)
    rmse = np.sqrt(mean_squared_error(true,predicted))
    return mae,r2,mse,rmse