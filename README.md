# CUDA-Grayscale-Converter

This project is a Google Colab–friendly Python script that converts uploaded images to grayscale using PyTorch with GPU acceleration (CUDA). It automatically sets up input and output directories, allows users to upload multiple images at once, and detects GPU availability to speed up the process. The script applies the standard grayscale formula (0.299 * R + 0.587 * G + 0.114 * B) to each image, saving the processed outputs to a dedicated folder. It also includes batch processing capabilities, a side-by-side visual comparison of original and converted images using Matplotlib, and the option to download all processed files as a ZIP package. Designed to be simple and fast, this tool is ideal for anyone looking to process large sets of images with GPU acceleration in a Colab or Jupyter environment.

## Quick Start (Google Colab)

1. Upload `CUDA_Batch_Grayscale_Converter.ipynb` to [Google Colab](https://colab.research.google.com/)
2. Run all cells sequentially
3. Upload your images when prompted
4. View results and download processed images

## Features

- **Batch Processing**: Convert hundreds of images simultaneously
- **CUDA Accelerated**: GPU-optimized grayscale conversion using PyTorch
- **Multiple Formats**: Supports JPG, PNG, BMP images
- **Visual Verification**: Before/after comparison
- **Performance Metrics**: GPU vs CPU benchmarking


## Usage

### Google Colab (Recommended)
1. Open the notebook in Colab
2. Run the first cell to install dependencies
3. Run the second cell to set up the environment
4. Upload images when prompted
5. Run the remaining cells to process and view results

### Local Execution (Requires CUDA-capable GPU)
```bash
pip install -r requirements.txt
python -m src.grayscale_converter
