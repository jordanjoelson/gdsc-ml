import pandas as pd
from pathlib import Path
from .create_subdirectory import subdirectories
import os
import shutil

# new_train_name: requires the new name for main directory
# data_csv: csv metadata of dataset
# train_path: path to the data to be categorize

def organize_data(new_train_name, data_csv, train_path):
    train = Path(train_path)
    data = pd.read_csv(data_csv)

    new_train_path = subdirectories(new_train_name, data.dx.unique())

    with os.scandir(train_path) as path:
        for current in path:
            if current.is_file():
                name = current.name.split('.')
                directory = data.loc[data["image_id"] == name[0]]
                shutil.move(train/current.name, new_train_path/directory["dx"].iloc[0])
    return new_train_path
