# import streamlit as st
import random

# st.title("GUESS NUMBER")

# ans = random.randint(1, 100)

# if "ans" not in st.session_state:
#     st.session_state.ans = random.randint(1, 100)

# num = st.text_input("please enter a number")
# test = 0

# while test == 0:
#     num = int(num)
#     ans = st.session_state.ans
#     if num < ans:
#         st.write("try bigger")
#     elif num > ans:
#         st.write("try smaller")
#     else:
#         st.write("you got it")
#         break

target = random.randint(1, 100)
while True:
    guess = int(input("please enter a number"))
    if guess < target:
        print("try bigger")
    elif guess > target:
        print("try smaller")
    else:
        print("you got it")
        break
