import os
import cv2
import numpy as np
import matplotlib.pyplot as plt


def inspect_image(image_path: str) -> dict:
    """Load the image and return its measured image-data properties."""

    image = cv2.imread(image_path)

    if image is None:
        raise FileNotFoundError(f"Could not load image: {image_path}")

    height, width, channels = image.shape

    pixel_count = width * height
    estimated_bytes = width * height * channels

    result = {
        "width": width,
        "height": height,
        "channels": channels,
        "shape": list(image.shape),
        "pixel_count": pixel_count,
        "estimated_bytes": estimated_bytes,
        "color_order": "BGR"
    }

    print("\n=== Task 1: Image Inspection ===")
    print(f"Width: {width}")
    print(f"Height: {height}")
    print(f"Channels: {channels}")
    print(f"Shape: {list(image.shape)}")
    print(f"Pixel count: {pixel_count}")
    print(f"Estimated data size: {estimated_bytes} bytes")
    print(f"Color order: BGR")

    return result


def create_pixel_views(image_path: str, output_dir: str) -> dict:
    """Create the labeled channel, grayscale, and downsampled views."""

    os.makedirs(output_dir, exist_ok=True)

    image = cv2.imread(image_path)

    if image is None:
        raise FileNotFoundError(f"Could not load image: {image_path}")

    height, width = image.shape[:2]

    # OpenCV loads images in BGR order
    blue_channel = image[:, :, 0]
    green_channel = image[:, :, 1]
    red_channel = image[:, :, 2]

    # Convert to grayscale
    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Downsample to half the original width and height
    downsampled_width = width // 2
    downsampled_height = height // 2

    downsampled = cv2.resize(
        image,
        (downsampled_width, downsampled_height),
        interpolation=cv2.INTER_AREA
    )

    output_path = os.path.join(output_dir, "pixel_views.png")

    # Create labeled montage
    fig, axes = plt.subplots(2, 3, figsize=(15, 9))

    axes[0, 0].imshow(red_channel, cmap="gray")
    axes[0, 0].set_title("Red Channel")

    axes[0, 1].imshow(green_channel, cmap="gray")
    axes[0, 1].set_title("Green Channel")

    axes[0, 2].imshow(blue_channel, cmap="gray")
    axes[0, 2].set_title("Blue Channel")

    axes[1, 0].imshow(grayscale, cmap="gray")
    axes[1, 0].set_title("Grayscale")

    # Convert BGR to RGB for correct display in Matplotlib
    downsampled_rgb = cv2.cvtColor(downsampled, cv2.COLOR_BGR2RGB)

    axes[1, 1].imshow(downsampled_rgb)
    axes[1, 1].set_title(
        f"Downsampled\n{downsampled_width} × {downsampled_height}"
    )

    axes[1, 2].axis("off")

    for ax in axes.flat:
        ax.axis("off")

    fig.suptitle("Task 2: Color Channels and Resolution", fontsize=16)

    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close(fig)

    result = {
        "original_size": [width, height],
        "downsampled_size": [downsampled_width, downsampled_height],
        "output_path": output_path
    }

    print("\n=== Task 2: Pixel Views ===")
    print(f"Original size: [{width}, {height}]")
    print(
        f"Downsampled size: "
        f"[{downsampled_width}, {downsampled_height}]"
    )
    print(f"Output: {output_path}")

    return result


def create_adjustments(
    image_path: str,
    output_dir: str,
    brightness_delta: int = 40,
    contrast_factor: float = 1.5,
    threshold: int = 127,
) -> dict:
    """Create labeled brightness, contrast, and threshold results."""

    os.makedirs(output_dir, exist_ok=True)

    if not 0 <= threshold <= 255:
        raise ValueError("threshold must be between 0 and 255")

    image = cv2.imread(image_path)

    if image is None:
        raise FileNotFoundError(f"Could not load image: {image_path}")

    # Convert original image to grayscale
    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Brightness adjustment
    brighter = np.clip(
        grayscale.astype(np.int16) + brightness_delta,
        0,
        255
    ).astype(np.uint8)

    # Contrast adjustment
    higher_contrast = np.clip(
        grayscale.astype(np.float32) * contrast_factor,
        0,
        255
    ).astype(np.uint8)

    # Thresholding:
    # Pixels greater than threshold become white.
    # All other pixels become black.
    _, thresholded = cv2.threshold(
        grayscale,
        threshold,
        255,
        cv2.THRESH_BINARY
    )

    output_path = os.path.join(output_dir, "adjustments.png")

    # Create labeled montage
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))

    axes[0, 0].imshow(grayscale, cmap="gray")
    axes[0, 0].set_title("Original Grayscale")

    axes[0, 1].imshow(brighter, cmap="gray")
    axes[0, 1].set_title(
        f"Brighter (+{brightness_delta})"
    )

    axes[1, 0].imshow(higher_contrast, cmap="gray")
    axes[1, 0].set_title(
        f"Higher Contrast (×{contrast_factor})"
    )

    axes[1, 1].imshow(thresholded, cmap="gray")
    axes[1, 1].set_title(
        f"Thresholded (>{threshold} = White)"
    )

    for ax in axes.flat:
        ax.axis("off")

    fig.suptitle("Task 3: Image Adjustments", fontsize=16)

    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close(fig)

    result = {
        "brightness_delta": brightness_delta,
        "contrast_factor": contrast_factor,
        "threshold": threshold,
        "output_path": output_path
    }

    print("\n=== Task 3: Adjustments ===")
    print(f"Brightness delta: {brightness_delta}")
    print(f"Contrast factor: {contrast_factor}")
    print(f"Threshold: {threshold}")
    print(f"Output: {output_path}")

    return result


def create_blur_and_edges(
    image_path: str,
    output_dir: str,
    kernel_size: int = 5,
) -> dict:
    """Create labeled grayscale, mean-blur, and Sobel-edge results."""

    os.makedirs(output_dir, exist_ok=True)

    if kernel_size <= 0 or kernel_size % 2 == 0:
        raise ValueError(
            "kernel_size must be a positive odd integer"
        )

    image = cv2.imread(image_path)

    if image is None:
        raise FileNotFoundError(f"Could not load image: {image_path}")

    # Convert to grayscale
    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Mean blur
    blurred = cv2.blur(
        grayscale,
        (kernel_size, kernel_size)
    )

    # Sobel edges from original grayscale
    sobel_x_original = cv2.Sobel(
        grayscale,
        cv2.CV_64F,
        1,
        0,
        ksize=3
    )

    sobel_y_original = cv2.Sobel(
        grayscale,
        cv2.CV_64F,
        0,
        1,
        ksize=3
    )

    original_magnitude = cv2.magnitude(
        sobel_x_original.astype(np.float32),
        sobel_y_original.astype(np.float32)
    )

    original_edges = cv2.normalize(
        original_magnitude,
        None,
        0,
        255,
        cv2.NORM_MINMAX
    ).astype(np.uint8)

    # Sobel edges from blurred grayscale
    sobel_x_blurred = cv2.Sobel(
        blurred,
        cv2.CV_64F,
        1,
        0,
        ksize=3
    )

    sobel_y_blurred = cv2.Sobel(
        blurred,
        cv2.CV_64F,
        0,
        1,
        ksize=3
    )

    blurred_magnitude = cv2.magnitude(
        sobel_x_blurred.astype(np.float32),
        sobel_y_blurred.astype(np.float32)
    )

    blurred_edges = cv2.normalize(
        blurred_magnitude,
        None,
        0,
        255,
        cv2.NORM_MINMAX
    ).astype(np.uint8)

    output_path = os.path.join(
        output_dir,
        "blur_and_edges.png"
    )

    # Create labeled montage
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))

    axes[0, 0].imshow(grayscale, cmap="gray")
    axes[0, 0].set_title("Grayscale")

    axes[0, 1].imshow(blurred, cmap="gray")
    axes[0, 1].set_title(
        f"Mean Blur ({kernel_size} × {kernel_size})"
    )

    axes[1, 0].imshow(original_edges, cmap="gray")
    axes[1, 0].set_title(
        "Sobel Edges - Original Grayscale"
    )

    axes[1, 1].imshow(blurred_edges, cmap="gray")
    axes[1, 1].set_title(
        "Sobel Edges - Blurred Grayscale"
    )

    for ax in axes.flat:
        ax.axis("off")

    fig.suptitle("Task 4: Blur and Sobel Edges", fontsize=16)

    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close(fig)

    result = {
        "kernel_size": kernel_size,
        "output_path": output_path
    }

    print("\n=== Task 4: Blur and Edges ===")
    print(f"Kernel size: {kernel_size}")
    print(f"Output: {output_path}")

    return result


def run_lab(image_path: str, output_dir: str) -> dict:
    """Run Tasks 1–4 and return their results together."""

    task1 = inspect_image(image_path)

    task2 = create_pixel_views(
        image_path,
        output_dir
    )

    task3 = create_adjustments(
        image_path,
        output_dir
    )

    task4 = create_blur_and_edges(
        image_path,
        output_dir
    )

    return {
        "task1": task1,
        "task2": task2,
        "task3": task3,
        "task4": task4
    }


def main() -> None:
    """Run the lab using the required repository paths."""

    image_path = "images/original.jpg"
    output_dir = "outputs"

    os.makedirs(output_dir, exist_ok=True)

    run_lab(
        image_path,
        output_dir
    )


if __name__ == "__main__":
    main()