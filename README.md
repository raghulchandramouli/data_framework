# Data Framework for Image Inpainting

A sophisticated framework for generating dynamic masks and performing image inpainting using state-of-the-art diffusion models. This framework automates the process of creating diverse mask patterns and applying intelligent inpainting for image manipulation.

## Features

- **Dynamic Mask Generation**: Creates various types of masks including:
  - Rectangle shapes
  - Circular patterns
  - Elliptical shapes
  - Bacteria-like organic patterns
  - Freeform shapes with natural contours

- **Automated Inpainting Pipeline**: Utilizes advanced diffusion models for seamless image restoration
- **Configurable Parameters**: Easily customize mask generation and inpainting settings
- **COCO Dataset Integration**: Built-in support for the COCO dataset
- **Logging System**: Comprehensive logging for pipeline monitoring

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/raghulchandramouli/data_framework
   cd data_framework
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

The framework uses a YAML configuration file (`config.yaml`) to manage various settings:

```yaml
paths:
  coco_dir: "path/to/coco/dataset"
  mask_dir: "path/to/mask/output"
  inpainted_dir: "path/to/inpainted/output"

dataset:
  num_images_to_process: 100
  start_index: 0

mask:
  dilation_kernel: 15
  dilation_iterations: 5
```

## Usage

### Running the Pipeline


### Command Line Execution

You can run the pipeline directly from the command line:

```bash
python pipeline.py
```

To specify a custom configuration file:

```bash
python pipeline.py custom_config.yaml
```

### Python Script Execution

Alternatively, you can import and run the pipeline in a Python script:

```python
from pipeline import run_pipeline

# Run with default configuration
run_pipeline()

# Or specify a custom config file
run_pipeline("custom_config.yaml")
```

### Mask Generation

```python
from mask_generator import generate_dynamic_mask

generate_dynamic_mask(
    image_path="path/to/input/image.jpg",
    mask_path="path/to/output/mask.png"
)
```

### Inpainting

```python
from inpainting import inpaint_image

inpaint_image(
    pipe=your_inpainting_pipeline,
    image_path="path/to/input/image.jpg",
    mask_path="path/to/mask.png",
    output_path="path/to/output/inpainted.jpg"
)
```

## Components

### Mask Generator

The mask generator creates dynamic binary masks using various geometric shapes:

- **Rectangle**: Creates rectangular masks with random positions and sizes
- **Circle**: Generates circular masks with varying radii
- **Ellipse**: Produces elliptical masks with random orientations
- **Bacteria**: Creates organic, bacteria-like shapes using random points
- **Freeform**: Generates natural-looking irregular shapes

### Inpainting Pipeline

The inpainting system uses a state-of-the-art diffusion model to fill masked regions with contextually appropriate content. Key features include:

- Customizable prompt for guiding the inpainting process
- Adjustable strength parameter for controlling the intensity of changes
- Configurable number of inference steps for quality control

## Project Structure

```
├── config.py           # Configuration loading utilities
├── config.yaml         # Configuration settings
├── dataset_manager.py  # Dataset handling functions
├── inpainting.py       # Inpainting implementation
├── mask_generator.py   # Mask generation logic
├── pipeline.py         # Main pipeline orchestration
├── requirements.txt    # Project dependencies
└── utils.py           # Utility functions
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

[MIT License]