import yaml
import logging

"""
Configuration Module

This module handles loading configuration settings from a YAML file and sets up logging.
It Provides functions to load the configuration and initialize logging for the application.
"""

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
    
def setup_logging(logging_config):
    
    """
    Set up logging based on the provided configuration.

    Args:
        logging_config (dict): Logging configuration settings.
        
        Expected Keys:
            - level (str) : Logging level (e.g., "INFO", "DEBUG"). always DEFAULTS TO INFO
            - format (str) : Logging string format. Defaults to a standard format.
            
        Returns:
            logging,Logger: A configured logger instance.
    """

    level = getattr(logging, logging_config.get("level", "INFO").upper(), logging.INFO)
    logging.basicConfig(
        level=level,
        format=logging_config.get("format", "%(asctime)s - %(levelname)s - %(message)s"),
    )
    
    return logging.getLogger(__name__)