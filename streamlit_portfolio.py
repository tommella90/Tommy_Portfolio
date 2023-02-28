from pathlib import Path
import streamlit as st
from PIL import Image
import os
import base64
import streamlit.components.v1 as components
from io import BytesIO
import base64
import os

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "me4.jpg"


PAGE_ICON = ":🧊:"
NAME = "Tommaso Ramella"
DESCRIPTION = """
Data scientist & postdoctoral researcher in economics
"""
EMAIL = "tommaso.ramella90@gmail.com"

st.set_page_config(layout="wide",
                   initial_sidebar_state="expanded",
                   page_title="PORTFOLIO",
                   page_icon=":🧊:")

@st.cache(allow_output_mutation=True)
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

@st.cache(allow_output_mutation=True)
def get_img_with_href(local_img_path, target_url, width, height):
    img_format = os.path.splitext(local_img_path)[-1].replace('.', '')
    bin_str = get_base64_of_bin_file(local_img_path)
    html_code = f'''
        <a href="{target_url}">
            <img src="data:image/{img_format};base64,{bin_str}" width="{width}" height="{height}" />
        </a>'''
    return html_code


git_path = 'images/git.png'
git_link = "https://github.com/tommella90"
git = get_img_with_href(git_path, git_link, width=40, height=40)

lnkd_path = 'images/linkedin.png'
lnkd_link = "https://www.linkedin.com/in/ommaso-ramella"
lnkd = get_img_with_href(lnkd_path, lnkd_link, width=40, height=40)

kaggle_path = 'images/kaggle.png'
kaggle_link = "https://www.kaggle.com/tommasoramella"
kaggle = get_img_with_href(kaggle_path, kaggle_link, width=40, height=40)

col0, col1, col2, col3 = st.columns([6, 3, 3, 3], gap="medium")
with col0:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.markdown(f"Email: {EMAIL}")
    st.write("My curriculum:", "[here](https://tommella90-digital-cv-app-w845um.streamlit.app/)")

with col1:
    st.write("GITHUB")
    st.markdown(git, unsafe_allow_html=True)
with col2:
    st.write("LINKEDIN:")
    st.markdown(lnkd, unsafe_allow_html=True)
with col3:
    st.write("KAGGLE:")
    st.markdown(kaggle, unsafe_allow_html=True)


width = 400
height = 300

## PROJECTS
housing_path = 'images/file_0.0.jpg'
housing_link = "https://github.com/tommella90/milano-housing-price"
housing = get_img_with_href(housing_path, housing_link, width, height)

rsp_path = 'images/file_1.0.jpg'
rsp_link = "https://github.com/tommella90/Rock-Scissor-Paper-move-recognition"
rsp = get_img_with_href(rsp_path, rsp_link, width, height)

gd_path = 'images/file_2.0.jpg'
gd_link = "https://github.com/tommella90/Gradient-descent-Linear-Regression"
gd = get_img_with_href(gd_path, gd_link, 300, height)

spotify_path = 'images/file_3.0.jpg'
spotify_link = "https://tommella90-songrecommender-app-recommender-kbuo63.streamlit.app/"
spotify = get_img_with_href(spotify_path, spotify_link, width, height)


# OTHER PROJECTS
width = 400
height = 300
word_cloud_oath = 'images/drop_words.png'
word_cloud_link = "https://tommella90-word-count-generator-app-2tkhtd.streamlit.app/"
word_cloud = get_img_with_href(word_cloud_oath, word_cloud_link, 400, height)

sex_path = 'images/ci_plot.jpeg'
sex_link = "https://github.com/tommella90/Predicting-sexual-discrimination"
sex = get_img_with_href(sex_path, sex_link, width, height)

scatterplot_path = 'images/scatter_eg1.png'
scatterplot_link = "https://github.com/tommella90/Scatterplot-generator-Touchdesigner"
scatterplot = get_img_with_href(scatterplot_path, scatterplot_link, 300, 300)



# DESIGN
st.write("_______________________")

st.title("MY RECENT PROJECTS")
st.subheader("Click on the images to see the code")
st.write("_______________________")
col1, col2 = st.columns([5, 5], gap="large")
with col1:
    st.markdown("## ROCK SCISSOR PAPER RECOGNITION")
    st.markdown("Hand recognition with Mediapipe")
    st.markdown(rsp, unsafe_allow_html=True)
with col2:
    st.markdown("## HOUSING DATASET - WEB-SCPRAPING")
    st.markdown("I build a dataset of italian houses with Beautiful Soup")
    st.markdown(housing, unsafe_allow_html=True)

st.write("_______________________")
col1, col2 = st.columns([5, 5], gap="large")
with col1:
    st.markdown("## SONG RECOMMENDER APP")
    st.markdown("Song reccomendation with K-mean clustering and Spotify API")
    st.markdown(spotify, unsafe_allow_html=True)
with col2:
    st.markdown("## GRADIENT DESCENT - 3D")
    st.markdown("I used Touchdesigner to create a 3D visualization of the gradient descent alghoritm")
    st.markdown(gd, unsafe_allow_html=True)


st.write("_______________________")
st.title("Other projects")
col1, col2, col3 = st.columns([4, 4.5, 4], gap="small")
with col1:
    st.markdown("#### Predicting Sexual discrimination")
    #st.write("[link](https://github.com/tommella90/Predicting-sexual-discrimination)")
    st.markdown(sex, unsafe_allow_html=True)

with col2:
    st.markdown("#### Automatic word cloud generator")
    #st.write("[link](https://github.com/tommella90/Predicting-sexual-discrimination)")
    st.markdown(word_cloud, unsafe_allow_html=True)

with col3:
    st.markdown("#### Scatterplot plotter generator ")
    #st.write("[link](https://github.com/tommella90/Predicting-sexual-discrimination)")
    st.markdown(scatterplot, unsafe_allow_html=True)
