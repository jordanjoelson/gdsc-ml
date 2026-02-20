import pandas as pd
import os
from pathlib import Path

def subdirectories(directory_name, unique_values):
    directory_location = Path("data/" + directory_name)

    os.makedirs(directory_location, exist_ok=True)

    for unique in unique_values:
        os.makedirs(directory_location / unique, exist_ok=True)

    return directory_location