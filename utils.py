"""
Utility Module

This module provides helper functions for common tasks such as file handling,
logging, and error management.
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