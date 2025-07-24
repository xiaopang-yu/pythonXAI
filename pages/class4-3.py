import streamlit as st
import os
import time

st.title("SWEETY・SHOOPING")

if "products" not in st.session_state:
    st.session_state.products = {}

col_num = st.number_input("請輸入欄位數", min_value=1, max_value=5, value=3, step=1)

file_path = "image"
files = os.listdir(file_path)

for img in files:
    if img[:-4] not in st.session_state.products:
        st.session_state.products[img[:-4]] = {
            "image": f"{file_path}/{img}",
            "price": 10,
            "stock": 10,
        }

cols = st.columns(col_num)

index = 0
for name, detail in st.session_state.products.items():
    with cols[index % col_num]:
        st.image(
            st.session_state.products[name]["image"], use_container_width=True
        )  # use_container_width = True 表示欄位大小＝圖片大小
        st.write(" #### " + name)
        st.write("price : $ " + str(st.session_state.products[name]["price"]))
        st.write("stock :  " + str(st.session_state.products[name]["stock"]))
        if st.button("buy " + name):
            if st.session_state.products[name]["stock"] > 0:
                st.session_state.products[name]["stock"] -= 1
                st.success(f"已購買 {name}")
                time.sleep(1)
                st.rerun()
            else:
                st.error(f"{name} 庫存不足")
                time.sleep(2)
                st.rerun()
    index += 1


st.title("新增商品庫存")

col1, col2 = st.columns(2)
with col1:
    selected_product = st.selectbox("選擇商品", st.session_state.products.keys())
with col2:
    add_number = st.number_input(
        "新增庫存數量", min_value=1, max_value=100, value=1, step=1
    )
if st.button("新增庫存"):
    st.session_state.products[selected_product]["stock"] += add_number
    st.success(f"已新增 { add_number } 個 {selected_product} 至庫存")
    time.sleep(2)
    st.rerun()

st.write("目前商品庫存：")

for name, detail in st.session_state.products.items():
    st.write(f"{name} : {detail['stock']} 個")
    # st.write(f"{name} : {st.session_state.products[name]['stock']} 個")
