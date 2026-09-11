"""
Task 2: Environment Setup & Synthetic Image Matrix Creation
--------------------------------------------------------------
Builds a 300x400x3 uint8 array and fills each quadrant with a
solid color using 2D spatial slicing: [row_start:row_end, col_start:col_end].
"""

import numpy as np


def build_quadrant_image(height=300, width=400, channels=3) -> np.ndarray:
    img = np.zeros((height, width, channels), dtype=np.uint8)

    mid_h, mid_w = height // 2, width // 2

    img[0:mid_h, 0:mid_w] = [255, 0, 0]        # Top-Left: Red
    img[0:mid_h, mid_w:width] = [0, 255, 0]    # Top-Right: Green
    img[mid_h:height, 0:mid_w] = [0, 0, 255]   # Bottom-Left: Blue
    img[mid_h:height, mid_w:width] = [255, 255, 255]  # Bottom-Right: White

    return img


def main():
    img = build_quadrant_image()

    print("--- SYNTHETIC MATRIX METRICS ---")
    print(f"Array Shape (H, W, C) : {img.shape}")
    print(f"Data Type             : {img.dtype}")
    print(f"Total Elements        : {img.size:,} values")
    print(f"Memory Footprint      : {img.nbytes:,} bytes ({img.nbytes / 1024:.2f} KB)")

    # Optional: save/preview the image if Pillow is installed
    try:
        from PIL import Image
        Image.fromarray(img).save("quadrant_output.png")
        print("Saved preview: quadrant_output.png")
    except ImportError:
        pass


if __name__ == "__main__":
    main()