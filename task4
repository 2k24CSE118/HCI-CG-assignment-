"""
Task 4: Spatial Downsampling & Pixelation via Striding
----------------------------------------------------------
Downsamples an image using a stride (step) slice, then re-expands it
with np.repeat to visualize the resulting pixelation.
"""

import numpy as np
from PIL import Image


def downsample(img: np.ndarray, n: int) -> np.ndarray:
    """Keep every N-th pixel along rows and columns."""
    return img[::n, ::n, :]


def reexpand(small_img: np.ndarray, n: int) -> np.ndarray:
    """Blow the downsampled array back up to the original size."""
    return np.repeat(np.repeat(small_img, n, axis=0), n, axis=1)


def main(image_path="sample.jpg", n=8):
    img = np.array(Image.open(image_path).convert("RGB"))

    small = downsample(img, n)
    expanded = reexpand(small, n)
    # Trim/pad in case the original dims aren't evenly divisible by n
    expanded = expanded[: img.shape[0], : img.shape[1], :]

    orig_bytes = img.nbytes
    small_bytes = small.nbytes

    dim_reduction = (1 - (small.shape[0] * small.shape[1]) /
                      (img.shape[0] * img.shape[1])) * 100
    # Per-axis reduction (matches the lab's "reduction per axis" framing)
    per_axis_reduction = (1 - 1 / n) * 100
    memory_savings = (1 - small_bytes / orig_bytes) * 100

    print(f"--- DOWNSAMPLING ANALYSIS (N = {n}) ---")
    print(f"Original Shape     : {img.shape} | Memory: {orig_bytes:,} bytes")
    print(f"Downsampled Shape  : {small.shape} | Memory: {small_bytes:,} bytes")
    print(f"Re-expanded Shape  : {expanded.shape} | Visual: Blocky Pixelation")
    print(f"Dimension Reduction: {per_axis_reduction:.2f}% reduction per axis")
    print(f"Memory Savings     : {memory_savings:.2f}% data reduction")

    Image.fromarray(expanded).save("task4_pixelated.png")
    print("Saved figure: task4_pixelated.png")


if __name__ == "__main__":
    main()