import streamlit as st

st.title("column component practice")
col1, col2 = st.columns(2)
col1.button("button 01")
col2.button("button 02")

col3, col4, col5 = st.columns({1, 2, 3})
with col3:
    st.write("column 03")
    st.button("button 03")
with col4:
    st.write("column 04")
    st.button("button 04")
with col5:
    st.write("column 05")
    st.button("button 05")


st.title("text input component practice")
text = st.text_input("please enter your content")
st.write("you just entered ' ", text, " ' ")

st.title("session state practice")
ans = 1
st.write(f"ans = {ans}")
if st.button("+1"):
    ans = ans + 1
st.write(f"ans = {ans}")

if "var1" not in st.session_state:
    st.session_state.var1 = 1
st.write(f"var1 = {st.session_state.var1}")
if st.button("add 1 to var1"):
    st.session_state.var1 = st.session_state.var1 + 1
    st.rerun()
