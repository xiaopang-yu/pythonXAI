import streamlit as st
import os

file_path = "image"
files = os.listdir(file_path)
st.write(files)

img_size = st.number_input("圖片大小", min_value=50, max_value=800, value=500, step=50)

for img in files:
    st.image(f"{file_path}/{img}", width=img_size)
