#implement hist equalisation, adaptive he, histogram matching
# sharpening, smoothening, gaussian blur
# linear filter


import streamlit as st
import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def compute_histogram(image):
    hist = np.zeros(256, dtype=int)
    for value in image.ravel():
        hist[value] += 1
    return hist


def compute_cdf(hist):
    cdf = hist.cumsum()
    cdf_normalized = cdf * (255 / cdf[-1])  # Normalize CDF to range [0, 255]
    return cdf_normalized


def apply_histogram_equalization(image, cdf_normalized):
    image_equalized = cdf_normalized[image].astype(np.uint8)
    return image_equalized


def load_image(image_file):
    image = Image.open(image_file).convert('L')  # Convert to grayscale ('L' mode)
    return np.array(image)


def histogram_equalization(image):
    # Compute histogram and CDF
    hist = compute_histogram(image)
    cdf_normalized = compute_cdf(hist)

    # Apply histogram equalization
    equalized_image = apply_histogram_equalization(image, cdf_normalized)
    return equalized_image


def invert_colors(image):
    return cv2.bitwise_not(image)


def calculate_histogram(image):
    hist = cv2.calcHist([image], [0], None, [256], [0, 256])
    return hist.flatten()


def plot_histogram(hist, title, color, ax):
    ax.plot(hist, color=color)
    ax.set_title(title)
    ax.set_xlim([0, 256])
    ax.set_xlabel('Pixel Intensity')
    ax.set_ylabel('Frequency')
    ax.grid(True)


def show_histograms(original_hist, transformed_hist):
    fig, axes = plt.subplots(1, 2, figsize=(16, 5))

    plot_histogram(original_hist, "Original Image Histogram", 'blue', axes[0])

    if transformed_hist is not None:
        plot_histogram(transformed_hist, "Transformed Image Histogram", 'red', axes[1])
    else:
        axes[1].set_visible(False)

    plt.tight_layout()
    return fig


def contrast_stretching(original_image):
    # Text input with default values and conversion to integers
    R_min = st.number_input("Enter the Rmin:", min_value=0, max_value=255, value=0)
    S_min = st.number_input("Enter the Smin:", min_value=0, max_value=255, value=0)

    R_max = st.number_input("Enter the Rmax:", min_value=0, max_value=255, value=255)
    S_max = st.number_input("Enter the Smax:", min_value=0, max_value=255, value=255)

    # Convert inputs to floats for calculation
    R_min = float(R_min)
    S_min = float(S_min)
    R_max = float(R_max)
    S_max = float(S_max)

    # Check for valid input ranges
    if R_max <= R_min:
        st.error("R_max must be greater than R_min.")
        return original_image
    if S_max <= S_min:
        st.error("S_max must be greater than S_min.")
        return original_image

    # Perform contrast stretching
    stretched_img = ((original_image - R_min) * (S_max - S_min) / (R_max - R_min) + S_min).astype(np.uint8)
    return stretched_img

st.title("Image Transformation App")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = load_image(uploaded_file)

    st.image(image, caption="Uploaded Image", use_column_width=True)

    transformation = st.selectbox("Select Transformation", [
        "None", "Histogram Equalization", "Power Transform", "Contrast Stretching"
    ])

    if transformation == "Histogram Equalization":
        transformed_image = histogram_equalization(image)

        st.image(transformed_image, caption="Transformed Image", use_column_width=True)
        original_hist = calculate_histogram(image)
        transformed_hist = calculate_histogram(transformed_image)

        fig = show_histograms(original_hist, transformed_hist)
        st.pyplot(fig)

    elif transformation == "Contrast Stretching":
        transformed_image = contrast_stretching(image)
        st.image(transformed_image, caption="Transformed Image", use_column_width=True)

    elif transformation == "Invert Colors":
        transformed_image = invert_colors(image)
    else:
        transformed_image = None
