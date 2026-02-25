from pathlib import Path
from tensorflow.keras.utils import image_dataset_from_directory

def get_train_data(train_path):
    
    train_data = image_dataset_from_directory(
        train_path,
        image_size = (380, 380),
        batch_size = 40,
        validation_split = .2,
        subset = "training",
        seed = 42,
        shuffle = True)
    
    return train_data

def get_test_data(test_path):

    test_data = image_dataset_from_directory(
        test_path,
        image_size = (380, 380),
        batch_size = 40,
        validation_split = .2,
        subset = "validation",
        seed = 42,
        shuffle = True)
    
    return test_data
