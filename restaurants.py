# streamlit run app.py

import streamlit as st
import pandas as pd
import numpy as np

DATA_URL = (r"< path >\zomato.csv")

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

# Restaurant data according to aggregate rating
st.header("Restaurants with rating higher than or equal to : ")
best_rated = st.slider("Rating :",0.0,5.0)
st.map(data.query("aggregate_rating >= @best_rated")[["latitude","longitude"]].dropna(how = "any"))

# Restaurants data according to price range
st.header(" Restaurants within a price range :")
st.markdown("The price range are represented by numbers from 1 to 4. "
	"From 1 being the lowest to 4 being the highest.")
price_range = st.selectbox("Range to look at :",range(1,5),1)
data = data[data['price range'] == price_range]

# Display Raw Data
st.subheader('Raw Data')
st.write(data)
