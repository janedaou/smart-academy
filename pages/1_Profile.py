import streamlit as st
from PIL import Image

# Load images
classroom_image = Image.open("assets/classroom.jpg")  # Replace with the path to your classroom image
logo_image = Image.open("assets/apgar_logo.jpg")  # Replace with the path to the APGAR logo

# App configuration
st.set_page_config(page_title="APGAR Smart Academy", layout="wide")

# Header section
st.image(logo_image, width=200)
st.title("Welcome to APGAR Smart Academy")
st.subheader("Empowering Growth, Inspiring Change")

# Login/Signup and Quiz buttons
st.markdown("##")
st.markdown("<div style='display: flex; flex-direction: column; align-items: center;'>", unsafe_allow_html=True)

if st.button("Login", key="login", help="Login", use_container_width=True):
    st.switch_page("pages/Sign_In.py")

st.markdown("<br>", unsafe_allow_html=True)  # Spacer

if st.button("Sign Up", key="sign_up", help="Sign UP", use_container_width=True):
    st.switch_page("pages/Sign_Up.py")

st.markdown("</div>", unsafe_allow_html=True)