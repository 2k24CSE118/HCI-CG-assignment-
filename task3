"""
Task 3: Channel Slicing & Isolation
---------------------------------------
Loads an image, extracts 2D intensity grids for R/G/B using Axis-2
slicing, builds single-channel color views, and displays a 2x3
matplotlib subplot grid (color row + grayscale row).
"""

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def load_image_array(path: str) -> np.ndarray:
    """Load an image file into a NumPy (H, W, 3) uint8 array."""
    return np.array(Image.open(path).convert("RGB"))


def extract_channels(img: np.ndarray):
    """Axis-2 slicing pulls out each 2D channel plane."""
    red_2d = img[:, :, 0]
    green_2d = img[:, :, 1]
    blue_2d = img[:, :, 2]
    return red_2d, green_2d, blue_2d


def isolate_channel(img: np.ndarray, channel_index: int) -> np.ndarray:
    """Zero out every channel except the one requested."""
    isolated = np.zeros_like(img)
    isolated[:, :, channel_index] = img[:, :, channel_index]
    return isolated


def main(image_path="sample.jpg"):
    img = load_image_array(image_path)
    red_2d, green_2d, blue_2d = extract_channels(img)

    red_only = isolate_channel(img, 0)
    green_only = isolate_channel(img, 1)
    blue_only = isolate_channel(img, 2)

    print("--- CHANNEL EXTRACTION SUMMARY ---")
    print(f"Original Image Shape  : {img.shape}")
    print(f"Red Channel 2D Shape  : {red_2d.shape} | Mean Intensity: {red_2d.mean():.2f}")
    print(f"Green Channel 2D Shape: {green_2d.shape} | Mean Intensity: {green_2d.mean():.2f}")
    print(f"Blue Channel 2D Shape : {blue_2d.shape} | Mean Intensity: {blue_2d.mean():.2f}")

    fig, axes = plt.subplots(2, 3, figsize=(12, 7))

    # Top row: color-isolated views
    axes[0, 0].imshow(red_only); axes[0, 0].set_title("Red-Only")
    axes[0, 1].imshow(green_only); axes[0, 1].set_title("Green-Only")
    axes[0, 2].imshow(blue_only); axes[0, 2].set_title("Blue-Only")

    # Bottom row: grayscale intensity maps
    axes[1, 0].imshow(red_2d, cmap="gray"); axes[1, 0].set_title("Red Intensity")
    axes[1, 1].imshow(green_2d, cmap="gray"); axes[1, 1].set_title("Green Intensity")
    axes[1, 2].imshow(blue_2d, cmap="gray"); axes[1, 2].set_title("Blue Intensity")

    for ax_row in axes:
        for ax in ax_row:
            ax.axis("off")

    plt.tight_layout()
    plt.savefig("task3_channel_grid.png", dpi=150)
    print("Display Window        : Matplotlib 2x3 Subplot Grid Rendered.")
    print("Saved figure: task3_channel_grid.png")


if __name__ == "__main__":
    main()