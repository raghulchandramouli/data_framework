"""
Inpainting Module

This module handles setting up and using the StableDiffusionInpaintPipeline for image inpainting.
It initializes the model and provides functionality for inpainting images.
"""

import torch
from diffusers import StableDiffusionInpaintPipeline
from config import load_config
from PIL import Image

config = load_config()

def setup_inpainting_pipeline():
    """
    Sets up the StableDiffusionInpaintPipeline for image inpainting.
    
    Returns:
        StableDiffusionInpaintPipeline: The initialized inpainting pipeline.
    """
    
    inpaint_config = config["inpainting"]
    pipe = StableDiffusionInpaintPipeline.from_pretrained(
        inpaint_config["model_name"],
        torch_dtype=getattr(torch, inpaint_config["torch_dtype"])
    )
    
    pipe = pipe.to(inpaint_config["device"])
    return pipe

def inpaint_image(pipe, image_path, mask_path, output_path):
    """
    Performs inpainting on an image using the provided pipeline.

    Args:
        pipe (StableDiffusionInpaintPipeline): The inpainting pipeline.
        image_path (str): Path to the input image.
        mask_path (str): Path to the mask image.
        output_path (str): Path to save the inpainted image.
    """
    image = Image.open(image_path).convert("RGB")
    mask = Image.open(mask_path).convert("L")
    
    # Perform inpainting
    inpainted_image = pipe(
        prompt="Fill the missing area with a natural, serene background",  # Prompt for inpainting
        image=image,
        mask_image=mask,
        strength=0.75,  # Strength of inpainting (0 to 1)
        num_inference_steps=50  # Number of diffusion steps
    ).images[0]

    # Save the inpainted image
    inpainted_image.save(output_path)
    
    