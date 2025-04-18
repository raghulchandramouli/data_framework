"""
Pipeline Module

This module orchestrates the execution of the data generation pipeline.
It handles dataset downloading, mask generation, and inpainting.
"""

import os
import argparse
from dataset_manager import download_and_extract_dataset
from mask_generator import generate_dynamic_mask
from inpainting import setup_inpainting_pipeline, inpaint_image
from config import load_config, setup_logging

def run_pipeline(config_path="config.yaml"):
    """
    Runs the entire data generation pipeline.

    Args:
        config_path (str): Path to the configuration file. Defaults to "config.yaml".
    """
    config = load_config(config_path)
    logger = setup_logging(config.get("logging", {}))

    # Download and extract dataset
    logger.info("Downloading and extracting dataset...")
    download_and_extract_dataset()

    # Setup inpainting pipeline
    logger.info("Setting up inpainting pipeline...")
    pipe = setup_inpainting_pipeline()

    # Process images
    logger.info("Generating masks and performing inpainting...")
    coco_dir = config["paths"]["coco_dir"]
    mask_dir = config["paths"]["mask_dir"]
    inpainted_dir = config["paths"]["inpainted_dir"]
    num_images_to_process = config["dataset"]["num_images_to_process"]
    start_index = config["dataset"]["start_index"]

    os.makedirs(mask_dir, exist_ok=True)
    os.makedirs(inpainted_dir, exist_ok=True)

    # Get list of images to process
    image_files = [f for f in os.listdir(coco_dir) if f.endswith((".jpg", ".png"))]
    image_files = image_files[start_index:start_index + num_images_to_process]

    for image_file in image_files:
        image_path = os.path.join(coco_dir, image_file)
        mask_path = os.path.join(mask_dir, f"mask_{image_file}")
        inpainted_path = os.path.join(inpainted_dir, f"inpainted_{image_file}")

        # Generate mask
        generate_dynamic_mask(image_path, mask_path)

        # Perform inpainting
        inpaint_image(pipe, image_path, mask_path, inpainted_path)

    logger.info("Pipeline execution completed.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=str, default="config.yaml", help="Path to the configuration file")
    args = parser.parse_args()
    run_pipeline(args.config)