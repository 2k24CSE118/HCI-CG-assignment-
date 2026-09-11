"""
Task 1: Display Pixel Density (PPI/DPI) Calculator
----------------------------------------------------
Computes total pixel count, simplified aspect ratio, DPI/PPI, and
classifies the display density.
"""

import math


def calculate_display_metrics(w_px: int, h_px: int, d_inches: float) -> dict:
    """Return total pixels, aspect ratio, and DPI for a given display."""
    total_pixels = w_px * h_px

    # Simplified aspect ratio using the greatest common divisor
    divisor = math.gcd(w_px, h_px)
    ratio_w, ratio_h = w_px // divisor, h_px // divisor

    # Diagonal pixel count (Pythagorean theorem) -> DPI
    diagonal_px = math.sqrt(w_px**2 + h_px**2)
    dpi = diagonal_px / d_inches

    return {
        "total_pixels": total_pixels,
        "aspect_ratio": f"{ratio_w}:{ratio_h}",
        "dpi": round(dpi, 2),
    }


def classify_density(dpi: float) -> str:
    """Classify display density per the lab's thresholds."""
    if dpi < 100:
        return "Low Density (Standard Monitor)"
    elif dpi <= 200:
        return "Medium Density (HD Display)"
    else:
        return "High Density (Retina / Mobile)"


def main():
    w_px = int(input("Enter horizontal resolution (pixels): "))
    h_px = int(input("Enter vertical resolution (pixels): "))
    d_inches = float(input("Enter physical diagonal size (inches): "))

    metrics = calculate_display_metrics(w_px, h_px, d_inches)
    category = classify_density(metrics["dpi"])

    print("\n--- DISPLAY METRICS ANALYSIS ---")
    print(f"Total Pixel Count : {metrics['total_pixels']:,} pixels")
    print(f"Aspect Ratio      : {metrics['aspect_ratio']}")
    print(f"Calculated DPI    : {metrics['dpi']} DPI")
    print(f"Density Category  : {category}")


if __name__ == "__main__":
    main()