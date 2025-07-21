import streamlit as st

st.title("標題")
st.write("內容")  # 數字、文字....
st.text("文字")  # 文字內容
st.markdown(
    """
  這是用markdown寫的字串  
  * 列點
  * **粗體
  * *斜體*
  * [連結名稱](網址本人)
  * 程式碼：
  ```python
    print("Hello, World!")
  ```
  # 標題一
  ## 標題二
  ### 標題三
  #### 標題四
  """
)
