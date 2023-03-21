import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
st.title("San Francisco trees")
trees_df = pd.read_csv("trees.csv")
st.write(trees_df.head())
df_dbh_grouped = pd.DataFrame(trees_df.groupby(['dbh']).count()['tree_id'])
df_dbh_grouped.columns = ['tree_count']
fig = px.histogram(trees_df['dbh'])
st.plotly_chart(fig)