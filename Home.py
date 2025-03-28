import streamlit as st
from PIL import Image
import pandas as pd

# Load images
classroom_image = Image.open("assets/classroom.jpg")  # Replace with the path to your classroom image
logo_image = Image.open("assets/apgar_logo.jpg")  # Replace with the path to the APGAR logo

# App configuration
st.set_page_config(page_title="APGAR Smart Academy", layout="wide")

# Header section
st.image(logo_image, width=200)
st.title("Welcome to APGAR Smart Academy")
st.subheader("Empowering Growth, Inspiring Change")

# Description
st.markdown(
    """  
    At **APGAR Smart Academy**, we believe in nurturing talent and fostering personal and professional growth.  
    Our innovative classes in coaching, project management, data analytics, personal development, and more are designed to 
    help you achieve your goals. Whether you're looking to enhance your career or explore your creative side, we have a course for you.  
    """
)

# Display the classroom image
st.image(classroom_image, caption="A glimpse of our learning environment.", use_container_width=True)

# Login/Signup and Quiz buttons
st.markdown("##")
st.markdown("<div style='display: flex; flex-direction: column; align-items: center;'>", unsafe_allow_html=True)

if st.button("Login / Signup", key="login", help="Go to the Profile page", use_container_width=True):
    st.switch_page("pages/1_Profile.py")  

st.markdown("<br>", unsafe_allow_html=True)  # Spacer

if st.button("Take Quiz to Find Your Course", key="quiz", help="Go to the Quiz page", use_container_width=True):
    st.switch_page("pages/2_Quiz.py")

st.markdown("</div>", unsafe_allow_html=True)

# Courses table
st.markdown("### Available Courses")
st.markdown(
    "Below is our schedule of exciting and enriching courses. Find the one that suits your interests and schedule, and start your journey of growth and learning."
)

# Course data
data = {
    "Course": [
        "Project Management",
        "Data Analytics",
        "Art Therapy – Drawing",
        "Coaching",
        "Acting Essentials",
        "How to Be a Better Person",
        "Communication Skills for Professionals",
        "Piano for Beginners",
    ],
    "Description": [
        "Learn the art of organizing, planning, and executing projects efficiently.",
        "Unlock the power of data to make informed decisions and drive success.",
        "Explore creativity and self-expression through therapeutic drawing sessions.",
        "Develop skills to mentor and inspire individuals to achieve their full potential.",
        "Master the fundamentals of acting and bring characters to life on stage.",
        "Cultivate kindness, empathy, and personal growth to become your best self.",
        "Enhance your ability to communicate effectively in personal and professional settings.",
        "Learn the basics of piano playing and start your musical journey.",
    ],
    "Schedule": [
        "Wednesdays, 3:00 PM - 5:00 PM",
        "Tuesdays and Fridays, 9:00 AM - 11:00 AM",
        "Mondays and Thursdays, 1:00 PM - 3:00 PM",
        "Mondays and Wednesdays, 10:00 AM - 12:00 PM",
        "Fridays, 6:00 PM - 8:00 PM",
        "Saturdays, 10:00 AM - 12:00 PM",
        "Thursdays, 6:00 PM - 9:00 PM",
        "Tuesdays and Thursdays, 2:00 PM - 4:00 PM",
    ],
}

# Create a DataFrame and display it as a table
courses_df = pd.DataFrame(data)
st.table(courses_df)
