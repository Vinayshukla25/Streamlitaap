import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# 0.configure the page
st.set_page_config(
    page_title="Data Science App",
    page_icon="💎",
    layout="wide"
)

# 1.load the data

@st.cache_data()
def load_data():
    url = 'data/Top_rated_movies1.csv'
    df = pd.read_csv(path, parse_dates=['release_date'])
    return df

# 2. build the UI
st.title("Data Science App")
with st.spinner("loading data...")
    df = load_data

st.header("IMDB 8000 movies dataset")
st.info("Raw Data in DataFrame")
st.dataframe(df, use_container_width=True)

st.success("Column information of the dataset")
cols = df.columns.tolist()
st.subheader(fTotal columns {len(cols)} 💎 {",".join(cols)})
# 3.odd some graph and widgets
st.header("Basic Data Visualization")             
# 4. adjust Layout

# how to run the app
# open terminal and run: