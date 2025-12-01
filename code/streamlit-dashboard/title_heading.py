import streamlit as st
from PIL import Image
 
def show_title_heading():
    st.subheader("🚗 📈 Auto-Insight: Predicting Ownership, Usage, Price and Insights from Indian Car Listings")
    st.markdown("""
<h4 style='text-align:center; font-size:18px; color:#333;'>DA 204o: Data Science in Practice</h4>
    """, unsafe_allow_html=True)
 
    # Display default car image
    image = Image.open("..\..\image\car.png")  # path relative to main app
    st.image(image, use_container_width=True)
 
    # Horizontal line
    st.markdown("<hr style='border:2px solid #007ACC; margin-top:0;'>", unsafe_allow_html=True)
 
    # Team info
    st.markdown("""
<p style='text-align:right; font-size:16px;'>
<b>By Team Data Pack</b><br>
<i>
    1. Binayak Chakraborty, Sony, binayakc@iisc.ac.in <br>
    2. Supratim Dey, Wipro, supratimdey@iisc.ac.in <br>
    3. Rohit Agarwal, Wipro, rohitagarwal@iisc.ac.in <br>
    4. Rituparno Chatterjee, Wipro, rituparnoc@iisc.ac.in
</i></p>
    """, unsafe_allow_html=True)
