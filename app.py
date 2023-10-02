import requests
import streamlit as st
from streamlit_lottie import st_lottie
from rich import print


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


def local_css(file_name):
    with open(file_name) as f:
        css_content = f.read()
        print("CSS Content:")
        print(css_content)
        st.markdown(f"<style>{css_content}</style>", unsafe_allow_html=True)


local_css("D:/Subhashini/Datascience/pest/style.css")




st.subheader("Hi, I am Khaja Mohideen :wave:")
st.title("A PEST CONTROL SERVICE PROVIDER")
st.write("""
Im Khaja Mohideen, the founder and owner of ERASE Pest Control Services. 
With a passion for pest management and a dedication to providing effective solutions, 
I've built a trusted name in the industry. With years of experience and a commitment 
to customer satisfaction, I lead a team of professionals who excel in tackling all 
your pest-related concerns. Our mission is to deliver top-notch pest control services 
with a focus on quality, safety, and eco-friendliness. We're here to help you enjoy a 
pest-free environment, whether it's in your home or business. Thank you for considering 
ERASE Pest Control Services for your pest control needs.
""")
st.write("[Learn More >](https://pythonandvba.com)")

#loading assets
lottie_coding =load_lottieurl("https://lottie.host/f3188099-228a-4cfe-bfbd-e3f5b88ed680/BpFet5AtOZ.json")

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            On my YouTube channel I am creating tutorials for people who:
            - are looking for a way to leverage the power of Python in their day-to-day work.
            - are struggling with repetitive tasks in Excel and are looking for a way to use Python and VBA.
            - want to learn Data Analysis & Data Science to perform meaningful and impactful analyses.
            - are working with Excel and found themselves thinking - "there has to be a better way."

            If this sounds interesting to you, consider subscribing and turning on the notifications, so you don’t miss any content.
            """
        )
        st.write("[YouTube Channel >](https://youtube.com/c/CodingIsFun)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/sathishmech1810@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()

