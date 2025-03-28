import streamlit as st
import cv2
import face_recognition as frg
import yaml
from utils import recognize, build_dataset

# Set up Streamlit page configuration
st.set_page_config(layout="wide")

# Load configuration
cfg = yaml.load(open('config.yaml', 'r'), Loader=yaml.FullLoader)
WEBCAM_PROMPT = cfg['INFO']['WEBCAM_PROMPT']

# Sidebar for settings
st.sidebar.title("Settings")

# Tolerance slider for face recognition
TOLERANCE = st.sidebar.slider("Tolerance", 0.0, 1.0, 0.5, 0.01)
st.sidebar.info(
    "Tolerance is the threshold for face recognition. The lower the tolerance, the stricter the recognition. "
    "The higher the tolerance, the more lenient the recognition."
)

# Sidebar for student information display
st.sidebar.title("Student Information")
name_container = st.sidebar.empty()
id_container = st.sidebar.empty()
name_container.info('Name: Unknown')
id_container.success('ID: Unknown')

# Main section for webcam input
st.title("Face Recognition App")
st.write(WEBCAM_PROMPT)

# Camera settings
cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

FRAME_WINDOW = st.image([])

# Capture and process frames from the webcam
try:
    while True:
        ret, frame = cam.read()
        if not ret:
            st.error("Failed to capture frame from camera")
            st.info("Please turn off other apps using the camera and restart this app.")
            break

        # Recognize faces in the frame
        image, name, id = recognize(frame, TOLERANCE)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Update student information in the sidebar
        name_container.info(f"Name: {name}")
        id_container.success(f"ID: {id}")

        # Display the webcam frame with recognition results
        FRAME_WINDOW.image(image)

        # Redirect to the quiz if a face is recognized
        if name != "Unknown":
            st.success(f"Welcome, {name}! Redirecting to the quiz...")
            st.switch_page("pages/2_Quiz.py")
            break
except Exception as e:
    st.error(f"An error occurred: {e}")
finally:
    # Release the webcam resource
    cam.release()

# Developer section in the sidebar
with st.sidebar.form(key='developer_section'):
    st.title("Developer Section")
    rebuild_button = st.form_submit_button(label='REBUILD DATASET')
    if rebuild_button:
        with st.spinner("Rebuilding dataset..."):
            build_dataset()
        st.success("Dataset has been reset.")
