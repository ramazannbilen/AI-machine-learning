import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Get data from form and write csv file")
name = st.text_input("enter name: ")
password = st.text_input("enter password: ", type = "password")
date_birth = st.date_input("enter birthdate:")
age = st.slider("Enter age: ", 1,100)
message = st.text_area("Enter message:" , height=80)

if st.button("Save"):
    ndf = pd.DataFrame({"Name": [name], 
                        "Password": [password],
                        "Date Birth": [date_birth],
                        "Age": [age],
                        "Message": [message]
                        })
    
    #st.write(ndf)
    ndf.to_csv("registration.csv", index=False)
st.divider()    