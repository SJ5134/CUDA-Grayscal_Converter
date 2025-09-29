# Standalone version of the Colab code
# Can run locally if you have CUDA setup
import os
import cv2
import numpy as np
import torch
import time

class GrayscaleConverter:
    def __init__(self, device=None):
        self.device = device or torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    
    def convert_batch(self, input_dir, output_dir):
        # Batch conversion implementation
        pass

if __name__ == "__main__":
    converter = GrayscaleConverter()
    converter.convert_batch('data/input', 'data/output')
