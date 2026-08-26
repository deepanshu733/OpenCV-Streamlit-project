import streamlit as st
import cv2
import numpy as np


st.set_page_config(
    page_title="OpenCV Image Processing",
    page_icon="🖼️",
    layout="wide"
)



st.title("🖼️ OpenCV Image Processing Dashboard")
st.write(
    "Upload an image, select an OpenCV operation, "
    "and compare the original and processed images."
)



st.sidebar.header("Image Processing")
operation = st.sidebar.selectbox(
    "Select Operation",
    [
        "Original",
        "Grayscale",
        "Blur",
        "Canny Edge Detection"
    ]
)

# Upload Image

uploaded_file = st.file_uploader(
    "Upload an image",
    type=["jpg", "jpeg", "png"]
)



# Image Processing

if uploaded_file is not None:

    # Read uploaded file
    file_bytes = np.asarray(
        bytearray(uploaded_file.read()),
        dtype=np.uint8
    )

    # Convert file into OpenCV image
    image = cv2.imdecode(
        file_bytes,
        cv2.IMREAD_COLOR
    )

    # Create a copy for processing
    processed_image = image.copy()


    
    # Apply Selected Operation
    

    if operation == "Grayscale":

        processed_image = cv2.cvtColor(
            image,
            cv2.COLOR_BGR2GRAY
        )

    elif operation == "Blur":

        processed_image = cv2.GaussianBlur(
            image,
            (7, 7),
            0
        )

    elif operation == "Canny Edge Detection":

        gray = cv2.cvtColor(
            image,
            cv2.COLOR_BGR2GRAY
        )

        processed_image = cv2.Canny(
            gray,
            100,
            200
        )


    # Display Images

    st.subheader("Image Comparison")

    col1, col2 = st.columns(2)

    with col1:

        st.write("### Original Image")

        st.image(
            image,
            channels="BGR",
            use_container_width=True
        )

    with col2:

        st.write("### Processed Image")

        if len(processed_image.shape) == 2:

            st.image(
                processed_image,
                use_container_width=True
            )

        else:

            st.image(
                processed_image,
                channels="BGR",
                use_container_width=True
            )


    # Image Information

    with st.expander("Image Information"):

        st.write("Operation:", operation)
        st.write("Width:", image.shape[1])
        st.write("Height:", image.shape[0])
        st.write("Channels:", image.shape[2])


    st.success(
        f"{operation} operation applied successfully!"
    )

else:
    st.info("Please upload an image to begin.")