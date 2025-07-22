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

with st.expander("class02課堂筆記"):
    st.write(
        """
    這裡是幫你整理的《Python 程式課筆記》，使用的是適合國小學生閱讀的語言和說明方式。希望你讀起來輕鬆、開心又能理解！

    ---

    # 🐍 Python 程式課筆記（第2堂）

    ## 🧠 我們今天學了什麼？

    ---

    ## 1️⃣ 比較運算子（比大小）

    這些符號可以用來比較數字大小或是否一樣：

    | 符號   | 意思       | 例子       | 結果      |
    | ---- | -------- | -------- | ------- |
    | `==` | 一樣嗎？     | `1 == 2` | ❌ False |
    | `!=` | 不一樣嗎？    | `1 != 2` | ✅ True  |
    | `>`  | 左邊比右邊大嗎？ | `3 > 2`  | ✅ True  |
    | `<`  | 左邊比右邊小嗎？ | `1 < 5`  | ✅ True  |
    | `>=` | 大於或等於嗎？  | `2 >= 2` | ✅ True  |
    | `<=` | 小於或等於嗎？  | `1 <= 0` | ❌ False |

    ---

    ## 2️⃣ 邏輯運算子（邏輯思考）

    用來判斷事情真假：

    | 語法               | 說明         | 結果      |
    | ---------------- | ---------- | ------- |
    | `not True`       | 把對的變成錯的    | ❌ False |
    | `not False`      | 把錯的變成對的    | ✅ True  |
    | `True and True`  | 兩個都要是對的才是對 | ✅ True  |
    | `True and False` | 有一個錯就錯     | ❌ False |
    | `True or False`  | 有一個對就對     | ✅ True  |
    | `False or False` | 全錯才錯       | ❌ False |

    ---

    ## 3️⃣ 練習：密碼驗證🔐

    輸入密碼，如果對了就顯示不同的人回家：

    ```python
    password = input("請輸入密碼：")
    if password == "0427":
        print("歡迎媽咪回家")
    elif password == "0713":
        print("歡迎把拔回家")
    elif password == "1102":
        print("歡迎胖胖回家")
    else:
        print("密碼錯誤，請重新輸入")
    ```

    ---

    ## 4️⃣ 判斷閏年（Leap Year）

    ### 什麼是閏年？

    每4年會有一年多一天（2月29日），那年就叫閏年。

    ### 判斷方法有三種寫法（意思一樣）：

    #### ✅ 寫法1：用分段的 `if` 判斷

    ```python
    if 年份 % 400 == 0:
        是閏年
    elif 年份 % 100 == 0:
        不是閏年
    elif 年份 % 4 == 0:
        是閏年
    else:
        不是閏年
    ```

    #### ✅ 寫法2：`if` 裡面再包 `if`

    #### ✅ 寫法3：一行寫完判斷條件（比較精簡）

    ```python
    if (年 % 4 == 0 and 年 % 100 != 0) or (年 % 400 == 0):
        是閏年
    ```

    ---

    ## 5️⃣ Streamlit 寫網頁程式（互動介面）

    ### 📌 輸入數字

    ```python
    number = st.number_input("請輸入數字：", min_value=0, max_value=100, step=2)
    st.write("你輸入的數字是：", number)
    ```

    ### 📌 判斷成績等級

    ```python
    if 分數 < 60：F
    elif 分數 < 70：D
    elif 分數 < 80：C
    elif 分數 < 90：B
    else：A
    ```

    ### 📌 按鈕點擊計數器（按10下會放氣球跟下雪）

    ```python
    if st.button("click me"):
        click_count += 1
        st.write(click_count)
        if click_count == 10:
            st.balloons()
            st.snow()
    ```

    ---

    ## 6️⃣ for 迴圈（重複做的工具）

    ```python
    for i in range(5):
        print(i)  # 從0數到4

    for i in range(2, 6):
        print(i)  # 從2數到5

    for i in range(2, 20, 3):
        print(i)  # 每次+3，從2開始
    ```

    ---

    ## 7️⃣ 練習：金字塔！

    ### 📌 數字金字塔

    ```
    1
    22
    333
    4444
    ```

    ```python
    for i in range(1, n+1):
        st.write(str(i) * i)
    ```

    ### 📌 箭頭金字塔

    ```
       *
      ***
     *****
    *******
       *
       *
    ```

    ---

    ## 8️⃣ 串列 List（放很多東西的盒子）

    ```python
    水果 = ["蘋果", "香蕉", "橘子"]
    數字 = [1, 2, 3, 4]
    混合 = ["蘋果", 1, True]

    巢狀 = [1, 2, 3, ["蘋果", "香蕉"]]
    print(巢狀[3][0])  # 會印出 "蘋果"
    ```

    ### 📌 串列切片（選一部分）

    ```python
    L = [1, 2, 3, "a", "b", "c"]
    print(L[1:4:2])  # 從第1個到第3個，每隔1個取一次
    print(L[::2])    # 全部，每隔1個取一次
    ```

    ---

    ## 🎉 結語

    今天我們學到了很多Python的基本概念，像是比大小、真假判斷、重複執行、還有怎麼做出互動式的網頁！這些工具就像魔法一樣，以後可以幫助你做出自己的小遊戲或網站哦！

    想像一下你以後可以自己寫出像寶可夢選單、點餐機、互動小測驗，都是靠這些基礎慢慢學起來的，加油 💪✨

    ---

    需要我幫你整理成可列印的版本、圖片說明版或做成互動式小卡也可以說喔！


    """
    )
