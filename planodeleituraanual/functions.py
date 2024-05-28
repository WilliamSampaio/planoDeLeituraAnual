import os

import pandas as pd
import streamlit as st


@st.cache_data
def load_biblia_df():
    return pd.read_json(os.path.join(os.getcwd(), 'biblia.df.json'))
