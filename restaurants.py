# streamlit run app.py

import streamlit as st
import pandas as pd
import numpy as np

DATA_URL = (r"\Users\adiimated\Desktop\python_app\zomato.csv")

st.title("Restaurants Around the World")
st.markdown("This application is a Streamlit dashboard that can be used"
	"to analyse restaurants in 15 countries as listed by zomato")

def load_data(nrows):
	data = pd.read_csv(DATA_URL, nrows=nrows, encoding='latin-1')
	data.dropna(subset=['Longitude','Latitude'],inplace = True)
	lowercase = lambda x: str(x).lower()
	data.rename(lowercase,axis='columns',inplace= True)
	return data

data = load_data(10000)

st.header("Where are the best rated restaurants in the world ?")
best_rated = st.slider("Rating :",0.0,5.0)
st.map(data.query("aggregate_rating >= @best_rated")[["latitude","longitude"]].dropna(how = "any"))


st.subheader('Raw Data')
st.write(data)
