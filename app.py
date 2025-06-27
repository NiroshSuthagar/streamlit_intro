import streamlit as st
import pandas as pd
from sklearn import datasets

df = pd.read_csv('cdc.csv')
st.write("Here's my first attempt at using streamlit and Pandas")
st.write(df)

df_plot = df.loc[df.gender == 'm',['height', 'weight']]

st.scatter_chart(
    df_plot
)



