import streamlit as st
import pandas as pd
import numpy as np
import time

st.title("Streamlit Feature Explorer")

st.header("Basic Streamlit Features")

st.write("This application demonstrates different Streamlit components.")

st.markdown("""
### Markdown Example
**Bold text**, *italic text*, and `code`.
""")



st.header("Text Input")

name = st.text_input("Enter your name:")

if name:
    st.write("Hello,", name)



st.header("Number Input")
age = st.number_input(
    "Enter your age:",
    min_value=1,
    max_value=100,
    value=21
)
st.write("Your age is:", age)



st.header("Selectbox")
operation = st.selectbox(
    "Select an operation:",
    ["Grayscale", "Blur", "Canny Edge", "Resize"]
)
st.write("Selected operation:", operation)


st.header("Multiselect")
skills = st.multiselect(
    "Select your skills:",
    [
        "Python",
        "NumPy",
        "Pandas",
        "OpenCV",
        "Machine Learning",
        "Deep Learning"
    ]
)
st.write("Selected skills:", skills)



st.header("Slider")
confidence = st.slider(
    "Select confidence:",
    0,
    100,
    50
)
st.write("Confidence:", confidence)


st.header("Checkbox")
learning = st.checkbox("I am currently learning Streamlit")
if learning:
    st.success("Keep learning!")


st.header("Radio Buttons")
level = st.radio(
    "Select your level:",
    ["Beginner", "Intermediate", "Advanced"]
)
st.write("Your level:", level)


st.header("Button")
if st.button("Click Me"):
    st.success("Button clicked successfully!")


st.header("File Uploader")
uploaded_file = st.file_uploader(
    "Upload an image:",
    type=["jpg", "jpeg", "png"]
)
if uploaded_file is not None:
    st.image(
        uploaded_file,
        caption="Uploaded Image"
    )


st.header("Video Display")
video_file = st.file_uploader(
    "Upload a video:",
    type=["mp4", "mov", "avi"]
)
if video_file is not None:
    st.video(video_file)


st.sidebar.title("Sidebar")
sidebar_option = st.sidebar.selectbox(
    "Choose an option:",
    ["Home", "Image Processing", "About"]
)
st.sidebar.write(
    "Selected:",
    sidebar_option
)



st.header("Columns")
col1, col2 = st.columns(2)
with col1:
    st.subheader("Column 1")
    st.write("Original Image")
with col2:
    st.subheader("Column 2")
    st.write("Processed Image")



st.header("Tabs")
tab1, tab2, tab3 = st.tabs(
    ["Python", "OpenCV", "Deep Learning"]
)
with tab1:
    st.write("Python section")
with tab2:
    st.write("OpenCV section")
with tab3:
    st.write("Deep Learning section")



st.header("Expander")
with st.expander("Click to see more information"):
    st.write(
        "This information is hidden inside the expander."
    )



st.header("Status Messages")
st.success("Success message")
st.info("Information message")
st.warning("Warning message")
st.error("Error message")



st.header("Progress Bar")
if st.button("Start Progress"):

    progress = st.progress(0)

    for i in range(101):
        time.sleep(0.01)
        progress.progress(i)

    st.success("Progress completed!")



st.header("Session State Counter")

if "count" not in st.session_state:
    st.session_state.count = 0

if st.button("Increase Counter"):
    st.session_state.count += 1

st.write(
    "Current count:",
    st.session_state.count
)


st.header("Basic Charts")

data = pd.DataFrame({
    "Epoch": [1, 2, 3, 4, 5],
    "Loss": [0.80, 0.60, 0.45, 0.30, 0.20],
    "Accuracy": [0.60, 0.70, 0.78, 0.86, 0.92]
})

st.subheader("Line Chart")

st.line_chart(
    data.set_index("Epoch")
)

st.subheader("Bar Chart")

st.bar_chart(
    data[["Loss", "Accuracy"]]
)


st.header("NumPy Data")

numbers = np.array([10, 20, 30, 40, 50])

st.write("NumPy Array:", numbers)
st.write("Mean:", numbers.mean())


st.success("Streamlit feature exploration completed!")