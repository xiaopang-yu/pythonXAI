---
## 🐍 Python 第五堂課筆記
---

## 📚【class5-1】：最簡單的「AI 聊天機器人」

### 💡 這段程式在做什麼？

1. 請你輸入一句話（像是：「你好」）
2. AI 聽到之後會回你一段話
3. 如果你打「exit」或「quit」，聊天就會結束

---

### 🔍 每行程式解釋

```python
import openai  # 告訴電腦，我要用 OpenAI 這個功能（讓 AI 聽得懂人話）
from dotenv import load_dotenv  # 讓電腦知道我們放了金鑰匙在 .env 這個秘密檔案裡
import os  # 幫我們找電腦的資料夾或讀金鑰

load_dotenv()  # 開始讀取 .env 裡面的東西

openai.api_key = os.getenv("OPENAI_API_KEY")  # 拿到金鑰，用來開啟 AI 功能
```

### 🧑‍💻 下面這一段是「聊天的主程式」

```python
while True:  # 一直重複做下面的事（直到你打 exit 為止）
    user_input = input("你：")  # 要你在終端機輸入一句話

    if user_input.lower() in ["exit", "quit"]:  # 如果你說的是 exit 或 quit（不管有沒有大小寫）
        break  # 就跳出這個聊天，不聊了
```

```python
    response = openai.chat.completions.create(
        model="gpt-4o-mini",  # 使用的是小版的 GPT-4 模型
        messages=[
            {"role": "system", "content": "請使用繁體中文進行後續對話"},  # 一開始就告訴 AI 要說中文
            {"role": "user", "content": user_input},  # 這是你剛剛說的話
        ],
    )
```

```python
    assistant_message = response.choices[0].message.content  # 把 AI 回的內容拿出來
    print(f"AI：{assistant_message}")  # 把它印在螢幕上
```

---

## 📚【class5-2】：會「記住聊天內容」的 AI

### 🤔 這有什麼不一樣？

它會把你跟 AI 說過的每句話都記起來，這樣 AI 就能接著上下文來回答！

---

### ✅ 新增的重點

```python
message = [{"role": "system", "content": "請使用繁體中文進行後續對話"}]  # 設定系統初始訊息
```

每次你說話的時候，就會把對話加進 message 裡：

```python
message.append({"role": "user", "content": user_input})  # 把你說的話加進對話內容
```

然後：

```python
response = openai.chat.completions.create(model="gpt-4o-mini", messages=message)
```

回完之後，也要把 AI 的回應加進去：

```python
assistant_message = response.choices[0].message.content
message.append({"role": "assistant", "content": assistant_message})
```

---

## 📚【class5-3】：用「網頁」來顯示對話！

### 🌟 這段是用 `streamlit` 做出像聊天框的畫面！

```python
import streamlit as st

st.chat_message("user").write("這是使用者的訊息")  # 顯示使用者說的話
st.chat_message("assustant").write("這是 AI 的回應")  # 顯示 AI 說的話
```

### ✨ 加入對話紀錄 history

```python
history = [
    {"role": "user", "content": "AI 你好"},
    {"role": "assistant", "content": "哈囉！找我有事嗎？"},
    {"role": "user", "content": "所以我說，那個醬汁呢？"},
    {"role": "assistant", "content": "蛤？"},
]
```

### 🖼️ 顯示歷史訊息（加上可愛頭像）

```python
for message in history:
    if message["role"] == "user":
        st.chat_message("user", avatar="🍄").write(message["content"])
    else:
        st.chat_message("assistant", avatar="🤖").write(message["content"])
```

---

## 📚【class5-4】：記住聊天內容（用 session）

### ✅ 用 session_state 儲存歷史紀錄

```python
if "history" not in st.session_state:
    st.session_state.history = []  # 建一個聊天記錄箱
```

每次使用者輸入，就會加進這個箱子裡：

```python
prompt = st.chat_input("請輸入訊息")
if prompt:
    st.session_state.history.append({"role": "user", "content": prompt})
    st.rerun()  # 重新整理頁面
```

---

## 📚【class5-5】：可以選 AI 模型 + 改訊息 + 清除聊天！

### 🧩 多了三個功能區：

```python
col1, col2, col3 = st.columns([5, 3, 1])  # 左中右三欄
```

- col1：讓你輸入系統訊息
- col2：可以選模型（像換角色）
- col3：🗑️ 按鈕可以清除聊天記錄

---

## 📚【class5-6】：上傳圖片給 AI 看！

### 📷 可以傳照片，問 AI「圖片裡是什麼？」

```python
uploaded_file = st.file_uploader("上傳圖片", type=["png", "jpg", "jpeg"])
```

圖片會轉成 base64（圖片的數字編碼格式）給 AI 看：

```python
base64_image = base64.b64encode(image_file.read()).decode("utf-8")
```

---

## 📚【class5-7】：海龜湯邏輯遊戲！

### 🐢 是什麼？

AI 會給一個奇怪的故事（題目），你只能問問題讓 AI 回「是」、「不是」或「沒關係」，猜出整個故事。

### 🧠 程式怎麼做的？

```python
with open("question/quizzes.json", "r", encoding="utf-8") as f:
    data = json.load(f)
    st.session_state.pick = random.randrange(len(data))
    quiz = data[st.session_state.pick]
```

會從 `quizzes.json` 裡隨機挑一題，然後設定規則：

```python
st.session_state.system_message = f"你是一位海龜湯遊戲的主持人，..."
```

---

## ✅ 總結：你今天學了什麼？

| 編號 | 主題                | 功能                    |
| ---- | ------------------- | ----------------------- |
| 5-1  | 最簡單的 AI 對話    | 可以跟 AI 說話          |
| 5-2  | 聊天會記憶          | AI 記得之前說過的話     |
| 5-3  | 用網頁顯示對話      | 有聊天框可以看          |
| 5-4  | 用 session 記錄對話 | 聊天記錄不會不見        |
| 5-5  | 加上選單和清除按鈕  | 可自訂模型、清空對話    |
| 5-6  | 傳圖片給 AI 看      | 問圖片內容是什麼        |
| 5-7  | 玩推理遊戲海龜湯    | AI 變主持人，你來猜故事 |

---
