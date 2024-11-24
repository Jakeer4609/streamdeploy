#web development using streamlit

import streamlit as st
import numpy as np
import pandas as pd
import joblib

st.title("promotion prediction app")

#read the dataset to fill the values in input

df=pd.read_csv('train_LZdllcl.csv')


#create input elements

department = st.selectbox("department",pd.unique(df['department']))
region = st.selectbox("region",pd.unique(df['region']))
education = st.selectbox("education",pd.unique(df['education']))
gender = st.selectbox("gender",pd.unique(df['gender']))
recruitment_channel = st.selectbox("recruitment_channel",pd.unique(df['recruitment_channel']))



no_of_trainings = st.number_input("no_of_trainings")
age = st.number_input("age")
previous_year_rating = st.number_input("previous_year_rating")
length_of_service = st.number_input("length_of_service")
KPIs_met_80 = st.number_input("KPIs_met >80%")
awards_won = st.number_input("awards_won?")
avg_training_score = st.number_input("avg_training_score")

inputs = {
    'department' : department,
    'region' : region,
    'education' : education,
    'gender' : gender,
    'recruitment_channel' : recruitment_channel,
    'no_of_trainings' : no_of_trainings,
    'age' : age,
    'previous_year_rating' : previous_year_rating,
    'length_of_service' : length_of_service,
    'KPIs_met >80%' : KPIs_met_80,
    'awards_won?' :awards_won,
    'avg_training_score' : avg_training_score
}

#load the model from pickel file

model = joblib.load('HR_promotion.pkl')

#action for submit button

if st.button('predict'):
    x_input = pd.DataFrame(inputs,index=[0])
    prediction = model.predict(x_input)
    st.write("Prdicted value is")
    st.write(prediction)
