"""
Configuration Module

This module handles loading configuration settings from a YAML file and sets up logging.
It Provides functions to load the configuration and initialize logging for the application.
"""

import yaml
import logging

def load_config(config_path = "config.yaml"):
    """
    Load configuration from a YAML file.
    
    Args:
        config_path (str): Path to the YAML configuration file.
        defaults to "config.yaml"

    Returns:
        dict: Configuration settings.
        
    Raises:
        FileNotFoundError: If the configuration file is not found.
        yaml.YAMLError: If there is an error parsing the YAML file.
    """
    
    with open(config_path, "r") as f:
        return yaml.safe_load(f)
    
