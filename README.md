# Apgar Smart Academy App

## Overview
The **Apgar Smart Academy App** is an innovative application designed to enhance the learning experience at the Apgar Smart Academy. The academy offers a diverse range of classes, including **coaching**, **project management**, **data analytics**, and **personal development**. This app leverages **facial recognition** technology to identify users and recommend personalized courses based on their interests, ensuring an individualized and seamless learning journey.

## Features

- **Facial Recognition for User Authentication**  
  Utilizes advanced facial recognition technology to securely identify users and log them into the app without needing to manually enter credentials.

- **Personalized Course Recommendations**  
  Based on the facial recognition data and the user's historical interactions, the app intelligently recommends courses aligned with their personal interests and learning goals.

- **Course Catalog**  
  Browse a wide selection of courses available at Apgar Smart Academy in fields such as **coaching**, **project management**, **data analytics**, and **personal development**. Each course comes with detailed descriptions and prerequisites.

- **User Profiles**  
  Users can create and manage their profiles, view recommended courses, track progress, and save courses for future learning.

- **Secure and Scalable Architecture**  
  Built with scalability in mind, the app ensures robust performance as the academy grows and offers a secure environment for users’ data.

## Technologies Used

- **Frontend**: Streamlit for a user-friendly interface and seamless interaction.
- **Backend**: Python for server-side logic and processing.
- **Database**: SQLite to store user data, course information, and history.
- **Facial Recognition**: OpenCV for real-time facial recognition to identify users and personalize their experience.
- **Natural Language Processing (NLP)**: Utilized to analyze user inputs and preferences to refine course recommendations.

## How to Use

1. **Sign Up/Login**  
   The first time you use the app, register with your details. After that, you can log in using **facial recognition** each time you visit.

2. **Browse Courses**  
   Navigate through the course catalog to explore available courses in coaching, project management, data analytics, and personal development.

3. **Receive Recommendations**  
   Once logged in, the app will recommend courses based on your profile and previous interactions. You can review and enroll in courses that suit your needs.

4. **Track Your Progress**  
   Keep track of the courses you’ve enrolled in and your progress. The app will suggest further learning materials based on your performance and interests.

## Installation

### Prerequisites
Make sure you have Python 3.6+ installed, along with the following dependencies:

- `streamlit`
- `opencv-python`
- `sqlite3`
- `PyPDF2`
- `nltk`

To install dependencies, run:
```bash
pip install -r requirements.txt
