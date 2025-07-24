---
## 🐍 Python 第四堂課筆記
---

### 🧠 1. 字典（dictionary）：像一本對照表

我們可以用「字典」來存放一組對應的資料，就像：

- 「apple」對應到「蘋果」
- 1 對應到「one」

```python
d = {"apple": "蘋果", 1: "one"}
print(d["apple"])  # 印出 蘋果
print(d[1])        # 印出 one
```

你可以：

- 用 `.keys()` 看有哪些 key（關鍵字）
- 用 `.values()` 看有哪些 value（值）
- 用 `.items()` 同時看 key 和 value

```python
for key in d.keys():
    print(key)

for value in d.values():
    print(value)

for key, value in d.items():
    print(f"{key}:{value}")
```

還可以：

- **改值**：`d[1] = "一"`
- **新增**：`d[4] = "four"`
- **刪除**：`d.pop(1)`
- **判斷有沒有**：`1 in d`（→ 有沒有 key 是 1）

---

### 🖼️ 2. 顯示圖片（用 Streamlit 做網頁）

你可以用 `streamlit` 做一個可以看圖片的網頁！

```python
import streamlit as st
import os

files = os.listdir("image")  # 找出 image 資料夾裡的所有圖片
img_size = st.number_input("圖片大小", min_value=50, max_value=800, value=500, step=50)

for img in files:
    st.image("image/" + img, width=img_size)
```

---

太棒了！我們現在來用**簡單又詳細的方式**說明你在 class4-3 做的購物網站程式。這個程式是用 Python 搭配 [Streamlit](https://streamlit.io) 工具製作的，可以讓你快速做出互動式的網頁商店！👛🛍️

---

## 🛒 3.我的購物網站

這個網站有兩大功能：

1. **可以買東西**（按按鈕扣庫存）
2. **可以補貨**（新增商品數量）

---

### 🔧 第一步：建立商品資料

```python
if "products" not in st.session_state:
    st.session_state.products = {}
```

- `st.session_state` 是 Streamlit 提供的「記憶區」，可以記住使用者的動作。
- 我們先檢查網站的記憶區裡有沒有 `products` 這個字典，如果沒有就建立一個空的字典 `{}`，用來儲存商品的資料。

---

### 📂 第二步：載入圖片

```python
file_path = "image"
files = os.listdir(file_path)
```

- 指定圖片資料夾是 `"image"`。
- 用 `os.listdir()` 把所有圖片檔案抓進來，例如 `apple.png`、`banana.png` 等。

---

### 🧸 第三步：建立商品資料結構

```python
for img in files:
    if img[:-4] not in st.session_state.products:
        st.session_state.products[img[:-4]] = {
            "image": f"{file_path}/{img}",
            "price": 10,
            "stock": 10,
        }
```

- `img[:-4]` 是拿掉圖片副檔名 `.png`、`.jpg`，例如 `"apple.png"` 變成 `"apple"`。
- 每個商品是這樣的結構：

```python
"apple": {
    "image": "image/apple.png",
    "price": 10,
    "stock": 10
}
```

📦 每個商品會包含：

- 圖片位置（image）
- 價格（price）
- 庫存數量（stock）

---

### 🖼️ 第四步：畫面排版（用欄位顯示商品）

```python
cols = st.columns(col_num)
```

- 使用 `st.columns()` 把頁面分成幾欄（欄數由使用者輸入）
- 然後把每個商品輪流放進去

---

### 🧨 第五步：顯示商品 + 購買功能

```python
with cols[index % col_num]:
    st.image(...)         # 顯示商品圖片
    st.write(...)         # 顯示商品名稱、價格、庫存
    if st.button("buy " + name):   # 點購買按鈕
        if stock > 0:
            減少庫存，顯示成功訊息
        else:
            顯示庫存不足
```

🔄 `index % col_num`：確保每個商品放在不同欄位裡（輪流放）

🛍 購買邏輯：

- 按下「buy」按鈕會檢查庫存
- 若庫存足夠就扣掉 1
- 顯示購買成功
- 重新整理畫面（`st.rerun()`）

🧯 如果庫存 = 0，就顯示錯誤訊息「庫存不足」

---

### 🧮 第六步：新增商品庫存

```python
selected_product = st.selectbox(...)  # 下拉選單選商品
add_number = st.number_input(...)     # 輸入要加多少庫存

if st.button("新增庫存"):
    st.session_state.products[selected_product]["stock"] += add_number
    st.success(...)
    st.rerun()
```

👆 這段讓你**補貨**：

- 選一個商品
- 輸入要增加的數量
- 按下按鈕，商品庫存就會變多！

---

### 📋 第七步：列出所有商品的目前庫存

```python
for name, detail in st.session_state.products.items():
    st.write(f"{name} : {detail['stock']} 個")
```

這段會列出目前每個商品還剩幾個，非常實用！

---

## ✅ 小結：整體流程圖

```text
1. 建立商品資料（從圖片檔名建立商品）
2. 顯示商品資訊（圖片 / 價格 / 庫存）
3. 買東西：按鈕 ➜ 庫存 -1 ➜ 顯示訊息
4. 新增庫存：選商品 + 數量 ➜ 加上去
5. 顯示目前所有商品庫存
```

---

### 🌟 想像你自己在經營一間雜貨店：

你可以放上：

- 🍎 商品圖片
- 💰 訂好價格
- 📦 設定庫存數量

然後你也能讓別人「線上購買」，點一下就可以賣出，還能幫商品補貨，這就是一個簡單的**購物網站的後台系統**！

---

### 👋 4. 函式（function）：把常做的事包起來

就像把動作「取名字」，以後只要叫名字就能執行這些動作。

```python
def hello():
    print("hello")

def hello_2(name):
    print("hello " + name)

def my_max(a, b):
    if a > b:
        return a
    else:
        return b
```

#### 🎯 圓形面積的計算

```python
def calculate_circle_area(r, pi=3.14, scale=1):
    return r ** 2 * pi
```

---

### 🧪 5. 變數作用範圍（Scope）

函式裡的變數和外面不一樣，要特別注意！像這樣：

```python
length = 10

def calculate_square_area():
    area = length ** 2  # 用外面的 length
    print("面積是", area)

calculate_square_area()
```

如果想改全域變數，要加 `global`：

```python
def calculate_square_area_3():
    global area
    area = length**2
```

---

### 📏 6. 計算兩點之間的距離

數學課有教過的距離公式可以用在程式裡！

```python
def distance(x1, y1, x2, y2):
    dis = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    return dis
```

---

### 🎲 7. 擲骰子遊戲

```python
import random

def roll_dice(n):
    result = []
    for i in range(n):
        num = random.randint(1, 6)
        result.append(num)
    return result
```

可以統計各個數字出現的次數：

```python
for k in outcome:
    if k == 1:
        count1 += 1
    ...
```

---

## 🎉 小結

| 主題       | 學到的技能                             |
| ---------- | -------------------------------------- |
| 字典       | 存 key-value、查找、改值、刪除、查有無 |
| Streamlit  | 做圖片網頁、做簡單購物網站             |
| 函式       | 定義功能、用參數、回傳值               |
| 變數範圍   | 函式內外變數的差別                     |
| 距離計算   | 使用數學公式                           |
| 擲骰子遊戲 | 隨機數、累加計算                       |

---
