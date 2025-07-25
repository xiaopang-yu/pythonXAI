import streamlit as st

st.chat_message("user").write("這是使用者的訊息")
st.chat_message("assustant").write("這是 AI 的回應")

history = [
    {"role": "user", "content": "AI 你好"},
    {"role": "assistant", "content": "哈囉！找我有事嗎？"},
    {"role": "user", "content": "所以我說，那個醬汁呢？"},
    {
        "role": "assistant",
        "content": "蛤？",
    },
]

for message in history:
    if message["role"] == "user":
        st.chat_message("user", avatar="🍄").write(message["content"])
    else:
        st.chat_message("assistant", avatar="🤖").write(message["content"])
