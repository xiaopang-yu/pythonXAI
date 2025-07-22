import streamlit as st

number = st.number_input("請輸入一個數字", min_value=0, max_value=100, step=1)

st.write(f"你輸入的入字是： {number}")
