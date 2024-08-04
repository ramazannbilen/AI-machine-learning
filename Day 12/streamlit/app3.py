import streamlit as st
import pandas as pd
import plotly.express as px
import pickle


st.title('Salary Prediction based on experience, grade and interview :heavy_dollar_sign:')

model = pickle.load(open("salary.pkl","rb"))

experience = st.number_input("Enter your experience: ", 1, 10)
grade  = st.number_input("Enter your grade: ", 1, 10)
interview = st.number_input("Enter your interview: ", 1, 20)

if st.button("Predict"):
    prediction = model.predict([[experience, grade, interview]])
    prediction = round(prediction[0][0],2)
    st.success(f"Salary Prediction: {prediction}")



