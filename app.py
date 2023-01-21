from pathlib import Path

import streamlit as st

from PIL import Image


# ---  PATH SETTINGS ----

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "asset" / "Vj Cv 2.pdf"
profile_pic = current_dir / "asset" / "My_photo.png"


# ------- GENERAL SETTINGS ---------

PAGE_TITLE = "Digital CV | VAIBHAV JAIN"
PAGE_ICON = ":wave:"
NAME = "VAIBHAV JAIN"
DESCRIPTION = """ Senior Design Engineer, Automating the iterative processes by developing algorithm."""

EMAIL = "vaibhavjain2395@gmail.com"
SOCIAL_MEDIA = {
    "Linkedin": "https://linkedin.com"
}

PROJECTS = {
    "Automation Web App - Automation of Design and Selection process of mechanical components with definite input parameters.": "#",
    "Automated Machine Diagnosis - Machine Diagnostic through vibration Analysis using Fast Fourier Transform with python.": "#",
    "Simulation & Analysis - Machine Diagnostic through vibration Analysis using Fast Fourier Transform.": "#",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# -------- LOAD CSS, PDF & PROFILE PIC ----
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --------- HERO SECTION -----
col1, col2 = st.columns(2, gap = "small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label = " Download resume",
        data = PDFbyte,
        file_name = resume_file.name,
        mime = "application/octet-stream",
    )
    st.write("@",EMAIL)

# --- SOCIAL LINKS -----

st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# -------EXPERIENCE & QUALIFICATION ----------

st.write("#")
st.subheader("Experience & Qualifications")
st.write(
    """
    - Strong hands on experience in Python and C++.
    - Adequate knowledge in Python data analysis.
    - Good understanding of time and space complexity of any Algorithm.
    - Excellent Team-player and Fast learner.
    """
)

# -------SKILLS ----------

st.write("#")
st.subheader("HARD SKILLS")
st.write(
    """
    - Python ( Pandas & Numpy lib), Tcl/Tk, Flask
    - C, C++, STL, Object-Oriented Programming in C++, Data Structures
    - HTML, CSS & Javascript
    - Ansys | Abaqus | ANSA | MATLAB & Simulink | MathCAD | PLM
    """
)


# ---------WORK HISTORY--------

st.write("#")
st.subheader("Work History")
st.write("---")

# ------------JOB 1--------------

st.write("**Senior Mechanical Design Engineer | TATA Advanced Systems Ltd, Bangalore(KA)**")
st.write("NOV 2020 - Present")
st.write(
    """
    - Development of Algorithms Scripts using Python and C++ to automate Mechanical Design processes.
    - Designed and developed various Defence weapon systems and machinery such as Akash Army Launcher, ATAGS, and Active Protection System for the Indian Army.
"""
)

st.write("**Mechanical Design Engineer | PBO Plus Consulting Services (P) Ltd, Nashik(MH)**")
st.write("MAY 2019 - APRIL 2020")
st.write(
    """
    - Developed an Algorithm on Python which converts Vibration time domain data into frequency domain for machine diagnosis through vibration analysis and control.
"""
)

st.write("**Mechanical Engineering Intern | Bharat Oman Refineries Ltd, Bina(MP)**")
st.write("JUNE 2017 - JULY 2017")
st.write(
    """
    - Responsible for Overhauling of Pumps, Compressors. Learned different aspects of machine maintenance.
"""
)


#------- PROJECTS & ACCOMPLISHMENTS -----------

st.write("#")
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")






