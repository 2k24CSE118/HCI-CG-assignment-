# Weeks 1–3 Image Processing Lab

## Introduction

This individual image-processing lab explores fundamental image-processing concepts using Python, OpenCV, NumPy, and Matplotlib.

The lab demonstrates how digital images can be inspected and processed using different techniques, including pixel analysis, color channels, image resolution, brightness adjustment, contrast adjustment, thresholding, image blurring, and Sobel edge detection.

A photograph taken by the student was used as the original input image.

---

## Objectives

The main objectives of this lab are to:

* Understand the basic structure of a digital image.
* Inspect image dimensions, channels, and pixel count.
* Understand RGB/BGR color channels.
* Convert a color image into grayscale.
* Reduce image resolution using downsampling.
* Adjust image brightness.
* Adjust image contrast.
* Apply binary thresholding.
* Apply mean blur to an image.
* Detect edges using the Sobel operator.
* Compare edge detection before and after blurring.
* Save processed image results for analysis.

---

## Technologies Used

* **Python**
* **OpenCV** (`opencv-python`)
* **NumPy**
* **Matplotlib**

---

## Project Structure

```text
HCI-CG-assignment-/
│
├── images/
│   └── original.jpg
│
├── outputs/
│   ├── pixel_views.png
│   ├── adjustments.png
│   └── blur_and_edges.png
│
├── weeks01-03_image_lab.py
├── requirements.txt
└── README.md
```

---

## Tasks Performed

### Task 1: Image Inspection

The original image is loaded using OpenCV and its basic properties are measured.

The program displays:

* Image width
* Image height
* Number of color channels
* Image shape
* Total number of pixels
* Estimated image data size
* Color channel order

OpenCV loads color images in **BGR (Blue, Green, Red)** order.

The total number of pixels is calculated using:

```text
Pixel Count = Width × Height
```

The estimated image data size is calculated using:

```text
Estimated Bytes = Width × Height × Number of Channels
```

---

### Task 2: Color Channels and Resolution

The program separates the original image into its three color channels:

* Red channel
* Green channel
* Blue channel

It also converts the original image into grayscale.

The image is then downsampled to half of its original width and height using OpenCV's `INTER_AREA` interpolation.

The generated result is saved as:

```text
outputs/pixel_views.png
```

This output contains:

* Red Channel
* Green Channel
* Blue Channel
* Grayscale image
* Downsampled image

---

### Task 3: Image Adjustments

The original image is converted to grayscale before applying different image adjustments.

The following operations are performed:

#### Brightness

The brightness is increased by adding a value of **40** to the grayscale pixel values.

```text
Brightness Delta = +40
```

Pixel values are limited to the valid range of **0–255**.

#### Contrast

The contrast is increased using a factor of:

```text
Contrast Factor = 1.5
```

The resulting values are also limited to the range of 0–255.

#### Thresholding

Binary thresholding is applied using a threshold value of:

```text
Threshold = 127
```

Pixels greater than the threshold become white, while the remaining pixels become black.

The generated result is saved as:

```text
outputs/adjustments.png
```

---

### Task 4: Blur and Sobel Edge Detection

The grayscale image is processed using a mean blur.

The blur uses a:

```text
5 × 5
```

kernel.

Sobel edge detection is then applied in both the horizontal and vertical directions.

The program calculates edge magnitude from the horizontal and vertical Sobel results.

Sobel edge detection is performed on:

1. The original grayscale image
2. The blurred grayscale image

This allows the effect of blurring on edge detection to be observed.

The generated result is saved as:

```text
outputs/blur_and_edges.png
```

---

## Output Files

### `pixel_views.png`

This output demonstrates:

* Red color channel
* Green color channel
* Blue color channel
* Grayscale conversion
* Image downsampling

### `adjustments.png`

This output demonstrates:

* Original grayscale image
* Increased brightness
* Increased contrast
* Binary thresholding

### `blur_and_edges.png`

This output demonstrates:

* Grayscale image
* Mean blurred image
* Sobel edges from the original grayscale image
* Sobel edges from the blurred grayscale image

---

## Installation

Make sure Python is installed on the computer.

Install the required Python libraries using:

```bash
pip install -r requirements.txt
```

The `requirements.txt` file contains:

```text
opencv-python
numpy
matplotlib
```

---

## How to Run the Program

### Step 1: Place the Original Image

Place the photograph inside the `images` folder and name it:

```text
original.jpg
```

The complete path should be:

```text
images/original.jpg
```

### Step 2: Open the Project

Open the `HCI-CG-assignment-` folder in VS Code.

### Step 3: Install Dependencies

Open the VS Code terminal and run:

```bash
pip install -r requirements.txt
```

### Step 4: Run the Python Program

Run:

```bash
python weeks01-03_image_lab.py
```

### Step 5: Check the Outputs

After the program finishes, the processed images will be available inside:

```text
outputs/
```

The program generates:

```text
pixel_views.png
adjustments.png
blur_and_edges.png
```

---

## Expected Result

After successfully running the program, the terminal displays information about the original image and the parameters used for each task.

The program also generates three labeled image montages containing the results of the image-processing operations.

These outputs demonstrate the practical application of basic image-processing techniques using Python.

---

## Conclusion

This lab provided practical experience with fundamental image-processing techniques.

The experiments demonstrated how an image can be inspected, separated into color channels, converted to grayscale, resized, adjusted for brightness and contrast, thresholded, blurred, and processed for edge detection.

The lab also demonstrated the use of OpenCV, NumPy, and Matplotlib for performing and visualizing image-processing operations in Python.
