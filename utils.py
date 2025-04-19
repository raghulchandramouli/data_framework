"""
Utility Module

This module provides helper functions for common tasks such as file handling,
logging, and error management.

Data Sanity Checking is done in this Module as well.
"""

import os
import logging
from typing import List

def create_directory(path: str) -> None:
    """
    Creates a directory if it doesn't already exist.

    Args:
        path (str): Path to the directory to create.
    """
    os.makedirs(path, exist_ok=True)

def get_image_files(directory: str) -> List[str]:
    """
    Retrieves a list of image files (JPEG, PNG) from a directory.

    Args:
        directory (str): Path to the directory containing images.

    Returns:
        List[str]: List of image file paths.
    """
    return [f for f in os.listdir(directory) if f.endswith((".jpg", ".png"))]

def log_error(message: str) -> None:
    """
    Logs an error message.

    Args:
        message (str): Error message to log.
    """
    logging.error(message)

def log_info(message: str) -> None:
    """
    Logs an informational message.

    Args:
        message (str): Informational message to log.
    """
    logging.info(message)


def filter_images_by_shape(image_paths: List[str]) -> List[str]:
    """
    Filters images by comparing their shapes to the first image's shape.

    Args:
        image_paths (List[str]): List of image file paths.

    Returns:
        List[str]: List of image paths with matching shapes.
    """
    import cv2
    valid_images = []
    reference_shape = None

    for img_path in image_paths:
        img = cv2.imread(img_path)
        if img is not None:
            if reference_shape is None:
                reference_shape = img.shape
                valid_images.append(img_path)
            elif img.shape == reference_shape:
                valid_images.append(img_path)

    return valid_images