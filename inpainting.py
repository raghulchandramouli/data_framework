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
    Sets up and initializes the StableDiffusionInpaintPipeline for image inpainting.
    
    This function:
    1. Loads inpainting configuration from the config file
    2. Initializes the pipeline with the specified model
    3. Configures the model's precision (float16 or float32)
    4. Moves the model to the specified device (CPU/GPU)
    
    Returns:
        StableDiffusionInpaintPipeline: Initialized inpainting pipeline ready for use
        
    Configuration Requirements:
        The config file should contain an "inpainting" section with:
        - "model_name": Name/path of the pretrained model
        - "torch_dtype": Precision setting ("float16" or "float32")
        - "device": Device to run the model on ("cuda" or "cpu")
    """
    
    inpaint_config = config["inpainting"]
    pipe = StableDiffusionInpaintPipeline.from_pretrained(
        inpaint_config["model_name"],
        torch_dtype=torch.float16 if inpaint_config["torch_dtype"] == "float16" else torch.float32
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
    
    