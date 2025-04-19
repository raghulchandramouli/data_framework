"""
Dataset Manager Module

This module handles downloading and extracting the COCO dataset.
It ensures the dataset is available locally for processing.
"""


import os
import requests
import zipfile
from config import load_config

config = load_config()

def download_and_extract_dataset():
    
    """
    Downloads and extracts the COCO dataset if it doesn't already exist.
    
    The dataset is downloaded from the URL specified in the config file and
    extracted to the directory specified in the config file.
    """
    
    dataset_dir = config["dataset"]["dataset_dir"]
    coco_url = config["dataset"]["coco_url"]
    stop_index = config["dataset"]["stop_index"]
    coco_zip = os.path.join(dataset_dir, "coco_val2017.zip")
    coco_dir = config["paths"]["coco_dir"]
    
    # Create dataset directory if it doesn't exist:
    os.makedirs(dataset_dir, exist_ok=True)
    
    # Download the dataset if it doesn't exist
    if not os.path.exists(coco_zip):
        print("Downloading COCO dataset...")
        response = requests.get(coco_url, stream=True)
        with open(coco_zip, "wb") as f:
            for chunk in response.iter_content(chunk_size=1024):
                f.write(chunk)

    # Extract the dataset if it hasn't been extracted
    if not os.path.exists(coco_dir):
        print("Extracting COCO dataset...")
        with zipfile.ZipFile(coco_zip, "r") as zip_ref:
            zip_ref.extractall(dataset_dir)