import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
import numpy as np
from streamlit_option_menu import option_menu
from annotated_text import annotated_text

st.set_page_config(page_title="Riad's Website",layout="wide")

def load_lottieurl(url: str) -> dict:
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()



def local_css(file_name: str) -> None:
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")
lottie_coding = load_lottieurl("https://lottie.host/98a8e3c3-c988-4f15-bfa1-92c42dfa2e02/1nSc2WS1lk.json")
ecommerce_project=Image.open("images/ecommerce-project-architecture.png")


#with st.sidebar:
#    selected= option_menu(
#        menu_title=None,
#        #menu_title="Navigation dashboard",
#        options=["Home","Projects","Chat","More"],
#        icons=["house","rocket-takeoff","chat","three-dots-vertical"],#https://icons.getbootstrap.com/
#        #menu_icon="rocket"
#        orientation="horizontal",
#        styles={
#            "nav-link":{
#                "color": "#000"
#            }
#        }
#    )


    
selected= option_menu(
        menu_title=None,
        #menu_title="Navigation dashboard",
        options=["Home","Projects","Chat","More"],
        icons=["house","rocket-takeoff","chat","three-dots-vertical"],#https://icons.getbootstrap.com/
        #menu_icon="rocket"
        orientation="horizontal",
        styles={
            "nav-link":{
                "color": "#000"
            }
        }
    )

if selected=="Home":
    with st.container():
        left,right=st.columns(2)
        with left:
            st.header("What I do")
            st.write("##")
            st.write(
                """
                some text
                here
                """
            )
            annotated_text(
            "This ",
            ("is", "Verb"),
            " some ",
            ("annotated", "Adj"),
            ("text", "Noun"),
            " for those of ",
            ("you", "Pronoun"),
            " who ",
            ("like", "Verb"),
            " this sort of ",
            ("thing", "Noun"),
            ". ",
            "And here's a ",
            ("word", ""),
            " with a fancy background but no label.",
        )
        with right:
            st_lottie(lottie_coding,key="yo")

if selected=="Projects":
    with st.container():
        st.write("---")
        image_column, text_column = st.columns((1, 2))
        with text_column:
            st.subheader("E-commerce Data Analysis Project")
            st.write("Create an advanced data engineering pipeline that processes and analyzes sales data from an e-commerce website using Apache Airflow for workflow management and ClickHouse as the high-performance data warehouse.")
            annotated_text(("Airflow", "","#faa"),("ETL", "","#fea"),("Clickhouse", "","#8ef"),("Ansible", ""),("Grafana", "","#fea"))
            st.markdown("[Explore the project](https://github.com/RiadBensalem/E-commerce-Sales-Analysis-Pipeline)")
        with image_column:
            st.image(ecommerce_project)

    with st.container():
        st.write("---")
        image_column, text_column = st.columns((1, 2))
        with text_column:
            st.subheader("E-commerce Data Analysis Project")
            st.write("Create an advanced data engineering pipeline that processes and analyzes sales data from an e-commerce website using Apache Airflow for workflow management and ClickHouse as the high-performance data warehouse.")
            st.markdown("[Explore the project](https://github.com/RiadBensalem/E-commerce-Sales-Analysis-Pipeline)")
        with image_column:
            st.image(ecommerce_project)
    
    with st.container():
        st.write("---")
        image_column, text_column = st.columns((1, 2))
        with text_column:
            st.subheader("Kubernetes Labs")
            st.write("Contains my solutions to the labs from the book \"Learn Kubernetes in a Month of Lunches\" ")
            st.markdown("[Explore the project](https://github.com/RiadBensalem/k8s-learning)")
        with image_column:
            st.image(ecommerce_project)


if selected=="Chat":
    with st.container():
        # Insert a chat message container.
        with st.chat_message("user"):
            st.write("Hello 👋")
            st.line_chart(np.random.randn(30, 3))

        st.chat_input("Say something") 

if selected=="More":
    with st.container():
        st.write("---")
        st.header("Get In Touch With Me!")

        contact_form = """
        <form action="https://formsubmit.co/94088c269e3af54b7ae77300b355e761" method="POST">
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