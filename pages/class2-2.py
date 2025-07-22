import streamlit as st

number = st.number_input("please enter a number : ", min_value=0, max_value=100, step=2)
st.write(f"the number you enter is： {number}")


# 練習：成績判斷
st.write("## practice")
score = int(
    st.number_input(
        "please enter your score : ", step=1, value=60, min_value=0, max_value=100
    )
)
if score < 60:
    grade = "F"
elif score < 70:
    grade = "D"
elif score < 80:
    grade = "C"
elif score < 90:
    grade = "B"
else:
    grade = "A"
st.write("you got grade " + grade)

if "click_count" not in st.session_state:
    st.session_state.click_count = 0
if st.button("click me"):
    st.session_state.click_count += 1
    st.write(st.session_state.click_count)
if st.session_state.click_count == 100:
    st.balloons()
    st.session_state.click_count = 0

if st.button("🎈"):
    st.balloons()
if st.button("❄️"):
    st.snow()
