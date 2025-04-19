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

    logger.info("Starting pipeline execution")

    try:
        # Download and extract dataset
        logger.info("Starting dataset download and extraction process")
        logger.debug(f"Downloading dataset from {config['dataset']['coco_url']}")
        download_and_extract_dataset()
        logger.info("Dataset download and extraction completed successfully")
        logger.debug(f"Extracted dataset available at {config['paths']['coco_dir']}")

        # Setup inpainting pipeline
        logger.info("Initializing inpainting pipeline")
        logger.debug(f"Using model: {config['inpainting']['model_name']}")
        pipe = setup_inpainting_pipeline()
        logger.info("Inpainting pipeline setup completed")
        logger.debug(f"Pipeline initialized with device: {config['inpainting']['device']}")

        # Process images
        logger.info("Starting image processing pipeline")
        logger.debug(f"Processing {num_images_to_process} images starting from index {start_index}")

        for idx, image_file in enumerate(image_files):
            logger.debug(f"Processing image {idx + 1}: {image_file}")
            logger.debug(f"Source image path: {image_path}")
            logger.debug(f"Mask output path: {mask_path}")
            logger.debug(f"Inpainted output path: {inpainted_path}")
            image_path = os.path.join(coco_dir, image_file)
            mask_path = os.path.join(mask_dir, f"mask_{image_file}")
            inpainted_path = os.path.join(inpainted_dir, f"inpainted_{image_file}")

            logger.info(f"Processing image {idx + 1}/{len(image_files)}: {image_file}")

            try:
                # Generate mask
                logger.debug(f"Generating mask for {image_file}")
                generate_dynamic_mask(image_path, mask_path)
                logger.debug(f"Mask generated successfully for {image_file}")

                # Perform inpainting
                logger.debug(f"Starting inpainting for {image_file}")
                inpaint_image(pipe, image_path, mask_path, inpainted_path)
                logger.debug(f"Inpainting completed for {image_file}")

            except Exception as e:
                logger.error(f"Error processing image {image_file}: {str(e)}")
                continue

            if (idx + 1) % 5 == 0:
                logger.info(f"Processed {idx + 1} images out of {len(image_files)}")

    except Exception as e:
        logger.error(f"Pipeline execution failed: {str(e)}")
        raise

    logger.info("Pipeline execution completed successfully")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=str, default="config.yaml", help="Path to the configuration file")
    args = parser.parse_args()
    run_pipeline(args.config)