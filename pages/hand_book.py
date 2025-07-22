import streamlit as st

with st.expander("class01課堂筆記"):
    st.write(
        """

    # 🐍 我的第一堂 Python 課筆記

    ## ✏️ 什麼是註解？

    寫程式時，我們可以加上說明，幫助自己或其他人看懂。這些說明叫做「註解」，電腦不會執行它！

    - **單行註解**：用 `#` 開頭
    👉 `# 這是一行說明文字`

    - **多行註解**：用三個 `\\\"""` 包起來
    👉

    ```python
    \\\"""
    這是
    多行
    註解
    \\\"""
    ```

    🪄 小技巧：按 `Ctrl + ?` 可以快速註解或取消註解很多行！

    ---

    ## 🖨️ 印東西出來：`print()`

    我們可以用 `print()` 把東西顯示出來！

    ```python
    print(100)        # 印出整數
    print(0.3124)     # 印出小數
    print(True)       # 印出布林值（True 或 False）
    print("hello")    # 印出文字（字串）
    ```

    ---

    ## 📦 變數：像小盒子一樣儲存東西

    ```python
    a = "hello"
    b = "world"
    print(a + " " + b)  # 印出 hello world

    c = 10
    d = 20
    print(c + d)        # 印出 30
    ```

    ---

    ## 🔁 改變變數的內容

    ```python
    x = 4
    x = x + 3   # 現在 x 變成 7
    x = x * 2   # 現在 x 變成 14
    print(x)
    ```

    ---

    ## 🧮 數學運算

    ```python
    print(7 + 3)     # 加法 → 10
    print(7 - 3)     # 減法 → 4
    print(7 * 3)     # 乘法 → 21
    print(7 / 3)     # 除法 → 2.333...
    print(7 // 3)    # 整數除法 → 2
    print(7 % 3)     # 餘數 → 1
    print(7**3)      # 次方 → 343
    ```

    🌟 特別注意：小數加法有時不太準

    ```python
    print(0.1 + 0.2)  # 可能會看到像 0.30000000000000004
    ```

    ---

    ## 🧵 文字處理（字串）

    ```python
    s1 = "hello"
    s2 = "world "
    print(s1 + s2)       # 合併 → hello world
    print(s1 + s2 * 2)   # s2 重複兩次

    name = "python"
    age = 31
    print(f"我是{name},今年{age}歲")  # f字串：把變數放進文字裡
    ```

    ---

    ## 📏 字串長度

    ```python
    print(len("hello"))  # 印出 5
    print(len(""))       # 印出 0（空字串）
    ```

    ---

    ## 🔍 看變數是什麼型別

    ```python
    print(type(True))     # bool（布林值）
    print(type(100))      # int（整數）
    print(type(123.0))    # float（小數）
    print(type("hello"))  # str（文字）
    ```

    ---

    ## 🔄 資料轉換

    ```python
    print(int(True))      # True → 1
    print(float(123))     # 整數變小數
    print(bool(""))       # 空字串 → False
    print(bool("hello"))  # 有內容的字串 → True
    ```

    ---

    ## ⌨️ 使用者輸入 input()

    可以讓使用者輸入資料，例如：

    ```python
    print("開始輸入姓名")
    a = input()   # 把使用者輸入的內容放到 a 裡
    print("你輸入的是", a)

    b = input("請輸入年齡：")  # 直接在畫面問問題
    print("你的年齡是", b, "歲")
    print(type(b))  # 注意：輸入的東西一開始都是文字！

    b = int(b)  # 把文字轉成整數
    print("兩年後你就", b + 2, "歲了")
    ```

    ---

    ## ⭕ 小挑戰：算圓面積

    ```python
    r = float(input("請輸入圓的半徑："))
    area = 3.14 * r ** 2
    print("圓面積是", area, "平方單位")
    print("圓面積是 " + str(area) + " 平方單位")
    print(f"圓面積是 {area} 平方單位")
    ```

    ---

    ## 🌐 streamlit：用 Python 做出簡單網頁

    ````python
    import streamlit as st

    st.title("這是網頁的標題")
    st.write("這是內文，可以是文字或數字")
    st.text("這是純文字")

    st.markdown(
        \\\"""
        這是用 Markdown 寫的文字格式語法
        * 這是列點
        * **粗體字**
        * *斜體字*
        * [點我開啟連結](https://example.com)

        程式碼範例：
        ```python
        print("Hello, World!")
        ```

        # 大標題
        ## 中標題
        ### 小標題
        #### 更小標題
        \\\"""
    )
    ````

    ---

    # 🎉 小結

    你今天學會了超多好玩的 Python 技巧！

    ✅ 用 `print()` 把東西印出來
    ✅ 學會變數、數學運算、文字處理
    ✅ 用 `input()` 和使用者互動
    ✅ 還玩了 `streamlit` 做小網頁！

    只要每天學一點點，你就會變成超強的程式小高手 💪
    加油！Python 等你來冒險 🚀🐍

    ---

    """
    )
