import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Do you want to be successfull? :100:")

st.slider("choose a num:" , 1, 100)

st.audio("data/song.mp3")

name = st.text_input("Please enter your name: ", max_chars=50)

st.success("Successfully")
st.error("Error")

df = pd.read_csv("data/prog_languages_data.csv")
fig = px.pie(df, values="Sum")
st.plotly_chart(fig)

fig2 = px.bar(df, x="lang",y = "Sum")
st.plotly_chart(fig2)

file = st.file_uploader("Upload Folder")

st.warning("not acceptable")
st.info("need more focus")

menu = ["Mainpage", "Machine Learning", "AI", "Data Science"]
st.sidebar.selectbox("Menu",menu)

st.code("""
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns
    import warnings
    warnings.filterwarnings(\"ignore\")\n
""")

#st.video("data/secret_of_success.mp4")
#st.camera_input("camera")

st.date_input("choose date")
st.time_input("choose time")
st.text_input("enter your password:", type= "password")
st.text_area("enter comments:", height=80)
st.number_input("enter your age:",1,100)
st.radio("choose marriage status:",("1","2"))
st.selectbox("Languages you know: ", ["Python", "SQL"])
st.multiselect("Languages you know: ", ["Python", "SQL"])
#st.video("http//"/video)
st.image("data/image_01.jpg")
st.divider()

df = pd.read_csv("data/iris.csv")
st.write(df)

st.area_chart(df)