import streamlit as st


# # 練習：數字金字塔

# st.write("## 練習：數字金字塔")
# n = st.number_input("請輸入金字塔的層數", max_value=9, step=1)
# n = int(n)
# for i in range(1, (n + 1)):
#     st.write(str(i) * i)


# 練習：箭頭金字塔

st.write("## 練習：箭頭金字塔")
r = st.number_input(
    "請輸入箭頭的層數",
    min_value=1,
    step=1,
)
r = int(r)
arrow = ""

for i in range(1, r + 1):
    arrow = arrow + (" " * (r - i) + "*" * (2 * i - 1) + "\n")
for i in range(r):
    arrow = arrow + (" " * (r - 1) + "*" + "\n")
st.write(
    f"""
```
{arrow}    
```
"""
)
