import requests
import streamlit as st
# from streamlit_lottie import st_lottie
from PIL import Image

# def load_lottieurl(url):
#     r = requests.get(url)
#     if r.status_code != 200:
#         return None
#     return r.json()
# lottie_coding = load_lottieurl("https://lottie.host/f3188099-228a-4cfe-bfbd-e3f5b88ed680/BpFet5AtOZ.json")
img_lottie_animation = Image.open("lottie_animation.png")


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")

# local_css("D:\Subhashini\Datascience\erase\style.css")

st.subheader("Hi, I am Khaja Mohideen:wave:")
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

#st.write("I'm Khaja Mohideen, the founder and owner of ERASE Pest Control Services. With a passion for pest management and a dedication to providing effective solutions, I've built a trusted name in the industry. With years of experience and a commitment to customer satisfaction, I lead a team of professionals who excel in tackling all your pest-related concerns. Our mission is to deliver top-notch pest control services with a focus on quality, safety, and eco-friendliness. We're here to help you enjoy a pest-free environment, whether it's in your home or business. Thank you for considering ERASE Pest Control Services for your pest control needs.")
st.write("[Learn More >](https://instagram.com/erase_pest_no1?igshid=MmU2YjMzNjRlOQ==)")

#loading assets
# lottie_coding =load_lottieurl("https://lottie.host/f3188099-228a-4cfe-bfbd-e3f5b88ed680/BpFet5AtOZ.json")

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            Residential Pest Control

1.**Elimination of pests in homes:**
- Customized solutions for homeowners
- Safe and effective treatments
- Commercial Pest Management

2.**Pest control services for businesses:**
- Tailored solutions for commercial spaces
- Minimizing disruptions to operations
- Pest Identification

3.**Expert pest diagnosis**
- Identification of pest species
- Accurate assessment of infestations
- Pest Extermination

4.**Swift and efficient pest removal**
- Proven pest control methods
- Safe and responsible extermination
- Preventative Services

5.**Prevention of future infestations**
- Customized prevention plans
- Ongoing maintenance and monitoring
- Expertise and Experience

6.**Experienced team of pest control professionals**
- Certified technicians
- In-depth knowledge of pest biology and behavior
- Service Areas

7.**Coverage areas and regions served by your business**
- Customer-Centric Approach

8.**Commitment to customer satisfaction**
- Tailoring services to meet unique needs
- Responsive customer support

9.**Why Choose Us**
- Years of industry experience
- Emphasis on safety and eco-friendliness
- Cost-effective pest control solutions
            """
        )
        st.write("[Instagram Profile >](https://instagram.com/erase_pest_no1?igshid=MmU2YjMzNjRlOQ==)")
    # with right_column:
    #     st_lottie(lottie_coding, height=300, key="coding")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/erasepestcontrolservices@gmail.com" method="POST">
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

