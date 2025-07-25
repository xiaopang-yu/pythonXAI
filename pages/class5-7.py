import streamlit as st
import openai
import json
import random

openai.api_key = st.secrets["OPENAI_API_KEY"]

with open("question/quizzes.json", "r", encoding="utf-8") as f:
    data = json.load(f)
    if "pick" not in st.session_state:
        st.session_state.pick = random.randrange(len(data))
    quiz = data[st.session_state.pick]

if "system_message" not in st.session_state:
    st.session_state.system_message = f"你是一位海龜湯遊戲的主持人，使用者為遊戲參與者 \n 面對使用者的提問你只能回答（是、否、無關），如果玩家的描述很接近正解，則輸出遊戲結束，並講述完整的正解 \n 題目：{quiz["title"]} \n 正解：{quiz["answer"]}"

if "model" not in st.session_state:
    st.session_state.model = "gpt-4o"

if "message" not in st.session_state:
    st.session_state.message = []

st.title("海龜湯")

col1, col2 = st.columns([4, 1])

with col1:
    st.session_state.model = st.selectbox("AI模型", ["gpt-4o", "gpt-4o-mini"])

with col2:
    if st.button("🗑️"):
        st.session_state.message = []
        st.rerun()

st.chat_message("assistant", avatar="🤖").write("題目：" + quiz["title"])
for message in st.session_state.message:
    if message["role"] == "user":
        st.chat_message("user", avatar="🍄").write(message["content"])
    else:
        st.chat_message("assistant", avatar="🤖").write(message["content"])

prompt = st.chat_input("請輸入訊息")
if prompt:
    st.session_state.message.append({"role": "user", "content": prompt})
    response = openai.chat.completions.create(
        model=st.session_state.model,
        messages=[
            {"role": "system", "content": st.session_state.system_message},
        ]
        + st.session_state.message,
    )

    assistant_message = response.choices[0].message.content
    st.session_state.message.append({"role": "assistant", "content": assistant_message})
    st.rerun()
