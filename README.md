# CUDA-Grayscal_Converter
This Python script converts uploaded images to grayscale using PyTorch with GPU (CUDA) acceleration. It auto-creates input/output folders, supports batch processing, applies the standard grayscale formula, shows side-by-side comparisons with Matplotlib, and lets users download all processed results as a ZIP file.

# CUDA Batch Grayscale Converter

A high-performance batch image processing tool that converts multiple images to grayscale using CUDA acceleration via PyTorch.

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
