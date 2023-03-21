import streamlit as st
import time
st.title("This is My First Streamlit App")
st.write("Hello,lets learn to build a streamlitapp")
import numpy as np
st.sidebar.write("This is mine")
check = st.sidebar.checkbox("Do you want to see the data?")
st.sidebar.radio("Pick the columns you want",['Col1','Col2','col3'])
st.multiselect("What options do you want?",['1','2'])
st.select_slider("Level of your knowledge",['Bad','Good','Excellent'])
st.slider("Select a number",0,50)
st.number_input("enter a number")
st.text_input("Enter your name")
st.text_area("Write a brief description about you?")
st.file_uploader("Upload a Csv file")
st.color_picker("Choose your favorite calor")
dataframe = np.random.randn(10, 20)
st.balloons()
st.progress(10)
with st.spinner("Wait for it.."):
    time.sleep(10)
if check == True:
    st.dataframe(dataframe)