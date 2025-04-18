"""
Masks Generator Module

This module handles the generations of dynamic masks for inpainting.
It creates random geometric shapes to mask out parts of an image.
"""

import cv2
import numpy as np
import random
from config import load_config

config = load_config()

def generate_dynamic_mask(image_path, mask_path):
    """
    Generates a dynamic binary mask using random geometric shapes.
    
    Args:
        image_path (str): Path to the input image.
        mask_path (str): Path to save the generated mask.
    """
    
    image = cv2.imread(image_path)
    h, w, _ = image.shape
    mask = np.zeros((h, w), dtype=np.uint8)
    shape_types = ["rectangle", "circle", "ellipse", "bacteria", "freeform"]
    
    def draw_shape(shape, mask):
        if shape == "rectangle":
            x = random.randint(50, max(50, w - 150))
            y = random.randint(50, max(50, h - 150))
            mask_size = random.randint(50, min(150, w - x - 50, h - y - 50))
            cv2.rectangle(mask, (x, y), (x + mask_size, y + mask_size), 255, -1)
        
        elif shape == "circle":
            center_x = random.randint(50, w - 50)
            center_y = random.randint(50, h - 50)
            radius = random.randint(25, min(100, center_x, center_y, w - center_x, h - center_y, 75))
            cv2.circle(mask, (center_x, center_y), radius, 255, -1)
            
        elif shape == "ellipse":
            center_x = random.randint(50, w - 50)
            center_y = random.randint(50, h - 50)
            axis_length1 = random.randint(25, 75)
            axis_length2 = random.randint(25, 75)
            angle = random.randint(0, 360)
            cv2.ellipse(mask, (center_x, center_y), (axis_length1, axis_length2), angle, 0, 360, 255, -1)
            
        elif shape == "bacteria":
            center_x = random.randint(100, w - 100)
            center_y = random.randint(100, h - 100)
            base_radius = random.randint(30, 60)
            num_points = random.randint(8, 20)
            angles = np.linspace(0, 2 * np.pi, num_points, endpoint=False)
            
            points = []
            
            for angle in angles:
                noise = random.uniform(0.7, 1.3)
                r = base_radius * noise
                x_val = int(center_x + r * np.cos(angle))
                y_val = int(center_y + r * np.sin(angle))
                
                points.append([x_val, y_val])

            points = np.array(points, dtype=np.int32)
            cv2.fillPoly(mask, [points], 255)
            
        elif shape == "freeform":
            margin = 100
            cx = random.randint(margin, w - margin)
            cy = random.randint(margin, h - margin)
            max_radies = random.randint(50, 100)
            num_points = random.randint(5, 15)
            points = []
            
            for _ in range(num_points):
                angle = random.random() * 2 * np.pi
                r = random.uniform(10, max_radius)
                x_val = int(cx + r * np.cos(angle))
                y_val = int(cy + r * np.sin(angle))
                points.append([x_val, y_val])

            points = np.array(points, dtype=np.int32)
            hull = cv2.convexHull(points)
            cv2.fillPoly(mask, [points], 255)
            
        return mask
    
    # Draw the first shape
    first_shape = random.choice(shape_types)
    mask = draw_shape(first_shape, mask)

    # With a 30% chance, add a second shape
    if random.random() < 0.3:
        second_shape = random.choice(shape_types)
        mask = draw_shape(second_shape, mask)

    # Dilate the mask to smooth edges
    kernel_size = config["mask"].get("dilation_kernel", 15)
    iterations = config["mask"].get("dilation_iterations", 5)
    kernel = np.ones((kernel_size, kernel_size), dtype=np.uint8)
    mask = cv2.dilate(mask, kernel, iterations=iterations)

    # Save the mask
    cv2.imwrite(mask_path, mask)