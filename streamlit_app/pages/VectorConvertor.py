import streamlit as st
import os
import sys

# Get the absolute path of the parent directory
parent_dir = os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), '..'))

# Add the parent directory to the Python path
sys.path.insert(0, parent_dir)

# Import the Vector_Convertor function from Vectorize_documentation.py
from streamlit_app.vectorize_documentation import Vector_Convertor

# Streamlit page configuration
st.set_page_config(page_title="Vector Converter", page_icon="", layout="centered")
st.title(" Convert Documents to Vectors")

# Button to execute the conversion
if st.button("Convert to Vectors"):
    try:
        progress_bar = st.progress(0)
        Vector_Convertor(lambda progress: progress_bar.progress(progress))
        st.success("Documents have been converted to vectors successfully!")
    except Exception as e:
        st.error(f"An error occurred: {e}")