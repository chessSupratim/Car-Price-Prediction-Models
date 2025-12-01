import streamlit as st
import pandas as pd
import title_heading, data_preview, analysis_visuals, model_evaluation, manual_input_prediction

# Custom CSS
st.markdown(
    """
<style>
    /* Page background and border */
    .stApp {
        background-color: #f9f9f9;  /* light skin color */
        border: 2px solid #007ACC;  /* blue border */
        border-radius: 10px;
        padding: 20px;
    }
 
    /* Optional: adjust main content padding */
    .main .block-container {
        padding: 2rem 2rem 2rem 2rem;
    }
</style>
    """,
    unsafe_allow_html=True
)

# SECTION 1: Title & Headings
title_heading.show_title_heading()
 
# SECTION 2: Data Preview
df = data_preview.show_data_preview("../../data/processed/CleanedCarDataset.csv")
 
# SECTION 3: Brand & Car Type Analysis & Price Visualizations
analysis_visuals.show_analysis_visuals(df)

# SECTION 4: Model Performance
st.markdown("### 🛠️🎯 Model Performance")
df_model = pd.read_csv("..\..\data\processed\model_performance.csv")
st.dataframe(df_model)

# SECTION 5: Models deployment & Evaluation
model_evaluation.show_model_evaluation(df)

# Section 6: Manual Input Car Price Prediction
manual_input_prediction.show_manual_input_prediction(df)



# Footer
st.markdown(
    """
<hr style="border:1px solid #ccc; margin-top:50px;">
<p style='text-align:center; font-size:14px; color:#555;'><b>
        © 2025 <i> Team Data Pack </i> | DA 204o- Course Project | IISC Bangalore - M.Tech(Online) 2025-2028
</b></p>
    """,
    unsafe_allow_html=True
)
