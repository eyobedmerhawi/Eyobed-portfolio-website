from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie
import streamlit.components.v1 as components

st.markdown("""
<style>

/* Make all containers scale better on small screens */
@media (max-width: 768px) {
    .css-1kyxreq, .css-1l02zno, .css-18e3th9 {
        padding-left: 10px !important;
        padding-right: 10px !important;
    }
}

/* Force columns to stack cleanly on mobile */
@media (max-width: 768px) {
    .block-container {
        padding-left: 1rem !important;
        padding-right: 1rem !important;
    }
}

/* Fix Streamlit column overflow issues */
@media (max-width: 768px) {
    .css-1r6slb0 {
        flex-direction: column !important;
    }
}

/* Make images scale perfectly */
img {
    max-width: 100% !important;
    height: auto !important;
}

/* Make Lottie animation scale on mobile */
@media (max-width: 768px) {
    .stMarkdown, .st-lottie, iframe {
        max-width: 100% !important;
    }
}

/* Mobile responsiveness for your custom contact card */
@media (max-width: 768px) {
    .contact-card {
        max-width: 100% !important;
        margin-left: 0 !important;
        padding: 18px !important;
        font-size: 16px !important;
    }
    .contact-icon {
        font-size: 22px !important;
    }
    .contact-link {
        font-size: 18px !important;
    }
}

</style>
""", unsafe_allow_html=True)


st.set_page_config(page_title="Eyobed's Personal Page", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

lottie_coding = load_lottieurl("https://lottie.host/bbc0ee2a-46be-4a1b-a615-22825e5c6f31/MsEHbGepxu.json")
img_resume = Image.open("Images/Resume.png")
img_certificate = Image.open("Images/Wells_Fargo_Certificate.png")

#Header
with st.container():
    st.subheader("Hello, I'm Eyobed Gebregziabher :wave:")
    st.title("A Cybersecurity and Software Engineering student at Georgia State University")
    st.write("[My LinkedIn>](https://www.linkedin.com/in/eyobed-gebregziabher-a353401b0/)")
    st.write("[My GitHub>](https://github.com/eyobedmerhawi)")

#What I do
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Get To Know Me")
        #st.write("##")
        st.write(
            """I'm a first-generation college student at Georgia State University, currently in my junior year pursuing a Bachelor’s degree 
            in Computer Science. With a strong passion for technology and a results-driven mindset, I am committed to seeing projects through 
            to successful completion. My academic journey has equipped me with the foundational skills in programming, systems analysis, and 
            software development, and I am particularly drawn to the field of cybersecurity. I believe that safeguarding information and 
            systems is essential in this day and age. As I continue to expand my knowledge and expertise, I am actively seeking internships and 
            collaborative opportunities to apply what I have learned and to further develop my skills in cybersecurity. I am excited about the 
            challenges ahead and the opportunity to make a meaningful impact in the tech industry."""
        )

    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# Resume and Certificates
with st.container():
    st.write("---")
    st.header("Resume And Certificates")

    # Side-by-side layout: resume left, certificate + text right
    resume_col, cert_col = st.columns((1, 1))

    # Left Column — Resume
    with resume_col:
        st.subheader("Resume")
        # You can tweak width as you like (or remove width to let Streamlit decide)
        st.image(img_resume, use_container_width=True)

    # Right Column — Certificate + Bullet Points
    with cert_col:
        st.subheader("Wells Fargo Certificate")
        st.image(img_certificate, use_container_width=True)

        st.write("""
**Participated in Wells Fargo's Software Engineering Job Simulation where I:**

- Understood requirements for building a system to manage financial portfolios  
- Identified essential data the system needed to track  
- Created an Entity Relationship Diagram (ERD)  
- Implemented the ERD using IntelliJ  
- Published the final implementation to GitHub  
""")

# Contact info
with st.container():
    st.write("---")
    st.header("Let's Keep in Touch")
    
    html_code = """
<style>
.contact-card {
    max-width: 600px;
    margin-left: 0;              /* Align left */
    padding: 25px;
    background-color: #01111fff; /* Your custom background color */
    border-radius: 12px;
    text-align: left;            /* Left-align text */
    transition: 0.3s ease;
    box-shadow: 0 4px 12px rgba(0,0,0,0.25);
    color: white;                /* Make text readable on dark bg */
}

.contact-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 20px rgba(0,0,0,0.35);
}

.contact-row {
    margin: 15px 0;
}

.contact-icon {
    font-size: 28px;
    margin-right: 10px;
}

.contact-link {
    font-size: 20px;
    color: #66aaff;
    text-decoration: none;
}

.contact-link:hover {
    text-decoration: underline;
}
</style>

<div class="contact-card">

    <h3 style="margin-bottom: 20px;">📬 Reach Out Anytime</h3>

    <div class="contact-row">
        <span class="contact-icon">📧</span>
        <a class="contact-link" href="mailto:eyobedmerhawi10@gmail.com" target="_blank" rel="noopener noreferrer">
            Email Me
        </a>
    </div>

    <div class="contact-row">
        <span class="contact-icon">💼</span>
        <a class="contact-link" href="https://www.linkedin.com/in/eyobed-gebregziabher-a353401b0/" 
           target="_blank" rel="noopener noreferrer">
            LinkedIn
        </a>
    </div>

    <div class="contact-row">
        <span class="contact-icon">🐙</span>
        <a class="contact-link" href="https://github.com/eyobedmerhawi" 
           target="_blank" rel="noopener noreferrer">
            GitHub
        </a>
    </div>

    <div class="contact-row">
        <span class="contact-icon">📸</span>
        <a class="contact-link" href="https://www.instagram.com/eyobedmerhawi10/" 
           target="_blank" rel="noopener noreferrer">
            Instagram
        </a>
    </div>

    <div class="contact-row">
        <span class="contact-icon">📍</span>
        <span style="font-size:20px;">Atlanta, GA</span>
    </div>

</div>
"""

components.html(html_code, height=600)

