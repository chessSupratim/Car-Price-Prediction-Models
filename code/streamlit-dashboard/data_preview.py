import streamlit as st

import pandas as pd
 
@st.cache_data

def load_data(path):

    return pd.read_csv(path)
 
def show_data_preview(path):

    df = load_data(path)

    st.markdown("### 𝄜 Data Preview")
 
    # Preview DataFrame

    with st.expander("The cleaned Cars DataFrame Preview (Year: 2000-2023):"):

        st.dataframe(df, use_container_width=True)
 
    st.markdown(f"**Number of rows:** {df.shape[0]}")

    st.markdown(f"**Number of columns:** {df.shape[1]}")
 
    return df  # Return dataframe for other sections


