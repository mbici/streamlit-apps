import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import pickle 

st.title("Palmer's Penguins")
penguins_df = pd.read_csv("penguins.csv")
penguins_df
selected_species = st.selectbox('What species would you like to visualize',
['Adelie', 'Gentoo', 'Chinstrap'])
selected_x_var = st.selectbox('What do want the x variable to be',
['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm',
'body_mass_g'])
selected_y_var = st.selectbox('What about the y?',
['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm',
'body_mass_g'])
species_df = penguins_df[penguins_df['species'] == selected_species]
fig,ax = plt.subplots()
ax = sns.scatterplot(x= selected_x_var,y= selected_y_var,data = species_df)
plt.title(f"Scatterplot of {selected_y_var} against {selected_x_var} for {selected_species}")
st.pyplot(fig)