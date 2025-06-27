import streamlit as st
import pandas as pd

df = pd.DataFrame({
    'name': ['Nirosh', 'Sam', 'Jane'],
    'scores': [36,45,54]
})

st.write("Here's my first attempt at using streamlit and Pandas")
st.write(df)