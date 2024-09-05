# implement hist equalisation, adaptive he, histogram matching
# sharpening, smoothening, gaussian blur
# linear filter


import streamlit as st
import cv2
import numpy as np
import matplotlib.pyplot as plt

def histogram_matching(source, reference):
    source_hist = compute_histogram(source)
    source_cdf = source_hist.cumsum()

    source_cdf = source_cdf/source_cdf[-1]

    source_cdf_norm = np.round(source_cdf*255).astype(np.uint8)

    reference_hist = compute_histogram(reference)
    reference_cdf = reference_hist.cumsum()

    reference_cdf = reference_cdf/reference_cdf[-1]

    reference_cdf_norm = np.round(reference_cdf*255).astype(np.uint8)

    lookup_table = np.zeros(256, dtype=np.uint8)
    
    # creating a lookup table
    j = 0  # index for reference CDF
    for i in range(256):
        while j < 256 and reference_cdf_norm[j] < source_cdf_norm[i]:
            j += 1
        lookup_table[i] = j
    matched_img = lookup_table[source]

    return matched_img

def adaptive_histogram_equalization(image, tile_size):
    height, width = image.shape  # dimensions

    output = np.zeros_like(image)

    # number of tiles
    num_tiles_x = width // tile_size
    num_tiles_y = height // tile_size

    # processing each tile
    for i in range(num_tiles_y):
        for j in range(num_tiles_x):

            # boundaries
            x_start = j * tile_size
            x_end = x_start + tile_size
            y_start = i * tile_size
            y_end = y_start + tile_size

            # extract the tile
            tile = image[y_start:y_end, x_start:x_end]

            tile = histogram_equalization(tile)

            # edit the output
            output[y_start:y_end, x_start:x_end] = tile

    return output


def compute_histogram(image):

    # calculating the frequency 
    hist = np.zeros(256, dtype=int)
    for value in image.flatten(): 
        hist[value] += 1
    return hist


def load_image(uploaded_file):
    # this part of the code was giving an error as varible was passing an object of streamlit class, 
    # hence we need to read the attribute of the variable    
    
    # read the content file, note that this is binary
    file_bytes = uploaded_file.read()
    
    # convert the binary file to a numpy array of decimal values
    np_arr = np.frombuffer(file_bytes, np.uint8)

    # This decodes the numpy array into an image format that OpenCV can work with.
    image = cv2.imdecode(np_arr, cv2.IMREAD_GRAYSCALE)
        
    return image


def histogram_equalization(image):
    # Compute histogram and CDF
    hist = compute_histogram(image)
    cdf = hist.cumsum()
    cdf_norm = cdf/cdf[-1]
    cdf_eq = np.round(cdf_norm*255).astype(np.uint8)
    equalised_img = cdf_eq[image]
    return equalised_img


def invert_colors(image):
    return cv2.bitwise_not(image)


def calculate_histogram(image):
    hist = np.zeros(256)
    for pixel in image.flatten():
        hist[pixel]+=1
    return hist


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

def power_transform(image, gamma, scaling_constant):
    img_float = image.astype(np.float32)  # optional for accuracy
    # REMEMBER TO NORMALIZE THE IMG_FLOAT VALUES FROM 0-1
    gamma_img = scaling_constant * np.power(img_float / 255.0, gamma)

    # change the number and clip irrelevant values
    gamma_img = np.clip(gamma_img * 255, 0, 255).astype(np.uint8)
    return gamma_img


st.title("Image Transformation App")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = load_image(uploaded_file)

    st.image(image, caption="Uploaded Image", use_column_width=True)

    transformation = st.selectbox("Select Transformation", [
        "None", "Histogram Equalization", "Adaptive Histogram Equalization", "Histogram Matching",
        "Power Transform", "Contrast Stretching", "Invert Colors"
    ])

    if transformation == "Histogram Equalization":
        transformed_image = histogram_equalization(image)

        st.image(transformed_image, caption="Transformed Image", use_column_width=True)
        original_hist = calculate_histogram(image)
        transformed_hist = calculate_histogram(transformed_image)

        fig = show_histograms(original_hist, transformed_hist)
        st.pyplot(fig)

    elif transformation == "Adaptive Histogram Equalization":
        tile_size = st.number_input("Enter the Smax:", min_value=1, max_value=255, value=1)
        transformed_image = adaptive_histogram_equalization(image, tile_size)
        st.image(transformed_image, caption="Transformed Image", use_column_width=True)

    elif transformation == "Histogram Matching":
        reference_file = st.file_uploader("Choose a reference image...", type=["jpg", "jpeg", "png"])
        if reference_file:
            reference = load_image(reference_file)
            st.write("The original source image is: ")
            st.image(image, caption="Original Source Image", use_column_width=True)

            st.write("The reference image is: ")
            st.image(reference, caption="Reference Image", use_column_width=True)

            output_image = histogram_matching(image, reference)

            st.image(output_image, caption="Transformed Image", use_column_width=True)

            # Calculate histograms for visualization
            original_hist = calculate_histogram(image)
            reference_hist = calculate_histogram(reference)
            output_hist= calculate_histogram(output_image)


            fig, axes = plt.subplots(1, 3, figsize=(16, 5))

            plot_histogram(original_hist, "Original Image Histogram", 'blue', axes[0])
            plot_histogram(reference_hist, "Reference Image Histogram", 'blue', axes[1])

            if output_hist is not None:
                plot_histogram(output_hist, "Transformed Image Histogram", 'red', axes[2])
            else:
                axes[1].set_visible(False)

            plt.tight_layout()
            st.pyplot(fig)

    elif transformation == "Contrast Stretching":
        transformed_image = contrast_stretching(image)
        st.image(transformed_image, caption="Transformed Image", use_column_width=True)

    elif transformation == "Power Transform":
        # st.slider("Gamma Value", min_value=-10, max_value=10, label_visibility="visible")
        gamma = st.slider("Select the value of gamma", -5.0, 100.0, 1.0)
        scaling_constant = st.number_input("Enter the scaling constant:", min_value=1, max_value=100, value=1)
        transformed_image = power_transform(image, gamma, scaling_constant)
        st.image(transformed_image, caption="Transformed Image", use_column_width=True)

    elif transformation == "Invert Colors":
        transformed_image = invert_colors(image)
        st.image(transformed_image, caption="Transformed Image", use_column_width=True)

    else:
        transformed_image = None
