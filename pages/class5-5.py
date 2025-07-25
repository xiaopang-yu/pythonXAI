import streamlit as st

if "system_message" not in st.session_state:
    st.session_state.system_message = "請用繁體中文進行後續對話"

if "model" not in st.session_state:
    st.session_state.model = "gpt-4o-mini"

if "message" not in st.session_state:
    st.session_state.message = []

st.session_state.system_message = st.text_input(
    "系統訊息", st.session_state.system_message
)

st.session_state.model = st.selectbox("AI模型", ["gpt-4o-mini", "gpt-4o"])

if st.button("🗑️"):
    st.session_state.message = []
    st.rerun()
