import streamlit as st  # For building web apps
from PyPDF2 import PdfReader  # For reading PDF files
import pandas as pd  # For data manipulation
import spacy  # For natural language processing
import numpy as np  # For numerical operations
from sklearn.metrics.pairwise import cosine_similarity  # For measuring vector similarity
from textblob import TextBlob  # For text processing and sentiment analysis
from nltk.corpus import wordnet  # For finding synonyms
import nltk  # For natural language processing tools
import sqlite3  # For database management
import re  # For regular expressions and pattern matching

# Apgar Logo and Page Title
st.image("assets/apgar_logo.jpg", width=150)
st.title("Welcome to APGAR Smart Academy!")
st.subheader("Discover your next learning adventure and find courses tailored to your interests.")

# Initialize the SQLite database
def initialize_database():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        face_encoding BLOB NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

initialize_database()

# Ensure NLTK's WordNet is downloaded
nltk.download('wordnet')

nlp = spacy.load("en_core_web_md")

def text_to_vector(text):
    return nlp(text).vector

def normalize_text(text):
    return text.lower().strip()

def correct_spelling(input_text):
    blob = TextBlob(input_text)
    return str(blob.correct())

def get_synonyms(word):
    synonyms = set()
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.add(lemma.name())
    return synonyms

# Parse the embedded PDF file
pdf_path = "assets/courses.pdf"

try:
    pdf_reader = PdfReader(pdf_path)
    extracted_text = ""

    # Extract text from all pages
    for page in pdf_reader.pages:
        extracted_text += page.extract_text()

    courses = []
    lines = extracted_text.split("\n")
    i = 0
    while i < len(lines):
        line = lines[i].strip()

        if line.startswith("Course:"):
            course_details = line.replace("Course:", "").strip()
            course_name, remaining = course_details.split(".", 1)
            course_name = course_name.strip()
            course_description = remaining.strip()

            # Collect full description
            while not course_description.endswith("."):
                i += 1
                if i < len(lines):
                    course_description += " " + lines[i].strip()
                else:
                    break

            # Find the line containing "Schedule:"
            i += 1
            schedule_line = lines[i].strip()
            schedule = re.sub(r'^Schedule\s*:\s*', '', schedule_line).strip()

            courses.append({
                "Course Name": course_name,
                "Description": course_description,
                "Schedule": schedule,
            })

        i += 1

    if courses:
        df_courses = pd.DataFrame(courses)

        with st.expander("Available Courses and Schedules"):
            st.dataframe(df_courses[["Course Name", "Description", "Schedule"]])

        # User input for availability and interests
        available_days = st.multiselect("What days are you available?", ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
        user_interest = st.text_input("What are you interested in learning?")
        threshold = st.slider("Set Similarity Threshold", 0.0, 1.0, 0.5, 0.1)

        if user_interest and available_days:
            corrected_user_input = correct_spelling(user_interest)
            normalized_user_input = normalize_text(corrected_user_input)

            user_words = normalized_user_input.split()
            expanded_input = set(user_words)
            for word in user_words:
                expanded_input.update(get_synonyms(word))
            expanded_user_input = " ".join(expanded_input)

            st.write("### Recommended Courses for You:")

            df_courses['Normalized_Course_Name'] = df_courses['Course Name'].apply(normalize_text)
            df_courses['Matches_Availability'] = df_courses['Schedule'].apply(lambda x: any(day in x for day in available_days))

            user_vector = text_to_vector(expanded_user_input)
            df_courses['Description_Vector'] = df_courses['Description'].apply(text_to_vector)

            df_courses['Similarity'] = df_courses['Description_Vector'].apply(
                lambda course_vector: cosine_similarity([user_vector], [course_vector])[0][0]
            )

            filtered_courses = df_courses[(df_courses['Matches_Availability']) & (df_courses['Similarity'] > threshold)]

            if not filtered_courses.empty:
                for _, row in filtered_courses.iterrows():
                    st.write(f"{row['Course Name']}")
                    st.write(f"{row['Description']}")
                    st.write(f"Schedule: {row['Schedule']}")
                    st.write(f"Similarity Score: {row['Similarity']:.2f}")
                    st.write("---")
            else:
                st.info("No relevant courses found. Try using different keywords or adjusting the similarity threshold.")
    else:
        st.warning("No course details found in the PDF. Please check the file format.")
except FileNotFoundError:
    st.error("The courses PDF file could not be found. Please ensure 'courses.pdf' is in the correct directory.")