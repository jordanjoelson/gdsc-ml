import tensorflow as tf
from src import get_train_data, organize_data, subdirectories
from models import get_model
import os
import pandas as pd

data_path = organize_data("new_train", "data/HAM10000_metadata.csv", "data/train")
data = get_train_data(data_path)
