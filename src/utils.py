import os
import sys

import numpy as np 
import pandas as pd
import dill
import pickle
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

from src.exception import CustomException

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)
    
def evaluate_models(X_train, y_train,X_test,y_test,models,param):
    try:
        report = {}

        for i in range(len(list(models))):
            model = list(models.values())[i]
            para=param[list(models.keys())[i]]

            gs = GridSearchCV(model,para,cv=3)
            gs.fit(X_train,y_train)

            model.set_params(**gs.best_params_)
            model.fit(X_train,y_train)

            #model.fit(X_train, y_train)  # Train model

            y_train_pred = model.predict(X_train)

            y_test_pred = model.predict(X_test)

            train_model_score = r2_score(y_train, y_train_pred)

            test_model_score = r2_score(y_test, y_test_pred)

            report[list(models.keys())[i]] = test_model_score

        return report

    except Exception as e:
        raise CustomException(e, sys)
    
def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)

    except Exception as e:
        raise CustomException(e, sys)

# def export_dataframe_to_csv(df, file_name):
#     current_dir = os.getcwd()
#     data_dir = os.path.join(current_dir, "data")
#     os.makedirs(data_dir, exist_ok=True)
#     file_path = os.path.join(data_dir, f"{file_name}.csv")
#     df.to_csv(file_path, index=False)
#     print(f"CSV file saved at: {file_path}")

# def evaluate_model(true,predicted):
#     mae = mean_absolute_error(true,predicted)
#     mse = mean_squared_error(true,predicted)
#     r2 = r2_score(true,predicted)
#     rmse = np.sqrt(mean_squared_error(true,predicted))
#     return mae,r2,mse,rmse