from pathlib import Path
import streamlit as st
from PIL import Image

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "cv_edgar_DC.pdf"
profile_pic = current_dir / "assets" / "for_cv1.png"
course_pic = current_dir / "assets" / "mfml.png"
cons_file = current_dir / "assets" / "constances.pdf"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Edgar Fragoso"
PAGE_ICON = "👤"
NAME = ":blue[Edgar] Fragoso"
DESCRIPTION = """I consider myself a driven individual with a 
                    passion for continuous growth and learning in :blue[Generative AI & MLops]."""
DESCRIPTION2= """This field is growing fast there are several tools for solving problems. I take training courses to be ready and resolve them with the best strategies."""
EMAIL = "edgarfragosogarcia@gmail.com"
SOCIAL_MEDIA = {
    
    "LinkedIn": "https://www.linkedin.com/in/edgar-omar-fragoso-garcia-69006092",
    "Twitch": "https://www.twitch.tv/edomfra",
    "GitHub": "https://github.com/edgarom"
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_resume:
    PDFbyte = pdf_resume.read()

with open(cons_file, "rb") as pdf_cons:
    PDFbyte1 = pdf_cons.read()

profile_pic = Image.open(profile_pic)
training_pic = Image.open(course_pic)

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="medium")
with col1:
    st.image(profile_pic, width=300)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📥 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("✉️", EMAIL)
    st.write("✉️", EMAIL2)
    

# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader(":blue[Experience] & Qulifications")
st.write(
    """
- ✔ 10 Years experience in Data Science.
- ✔ I Keep positive attitude to face new challenges. 
- ✔ Good understanding of mathematics and statistical principles.

"""
)
#------- ACCOMPLISHMENTS----------

st.write('\n')
st.subheader("Accomplishments")
st.write(
    """
- ⟡ I've expanded my expertise into the forefront of generative AI, focusing on the implementation of Optical Character Recognition (OCR) and Large Language Models (LLMs). I have spearheaded the development of virtual assistants powered by Retrieval-Augmented Generation (RAG). 
- ⟡ ntegrating module to AIopsHUB to predict crashes in node servers in bank systems through prophet forecasting module using CPUs and Memory as input. Furthermore, I Implemented a forecast for the Optimization of cash in branch banks an ATM. My knowledge let me bring Python courses with an aproach to Data Science to collaborators of Salinas Group.
- ⟡ The implementation of a pipeline in AWS and Linear Regularization Method allow to the company give valuable information to end users about the relation of genetic markers and clinical conditions, the above increased the flow of users the company increase gains in 2022.
- ⟡ The automatization of reports to end users in local servers of Clustering and Classification methods allowed to the company concentrate its efforts on the sales area..
- ⟡ The organization gave technical tools to farmers to resolve international controversies about the possible transmission of
pathogenic through foods with the rule of the FDA the above reduces the loss of millions of dollars to Mexican farmland. 
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Skills")
st.write(
    """
- ⚙ Programming: Python and Bash.
- ⚙ ML: Linear, Clasification, Clustering.
- ⚙ Cloud & MLOPs: Azure, AWS, Databricks.
- ⚙ OSys & DevOPS: Linux, Docker, Git. 
"""
)

#---------Courses-----------
st.write('\n')
st.subheader("Training")
col3, col4 = st.columns(2, gap="large")
with col3:
    st.image(training_pic, width=350)

with col4:
    st.write(DESCRIPTION2)
    st.download_button(
        label=" 📥 Download My Training",
        data=PDFbyte1,
        file_name=cons_file.name,
        mime="application/octet-stream",
    )
    





