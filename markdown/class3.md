---

# 🐍 Python 第三堂課筆記

## 📦 1. 列表（List）是什麼？

就像是裝東西的箱子，可以放好幾個資料（像是數字、文字...）

```python
print(len([]))  # 空箱子，長度是 0
print(["apple"])  # 裡面有一個蘋果
print(["a", "b"])  # 裡面有兩個東西
print(len([1, 2, 3]))  # 算算裡面有幾個東西：3 個
```

### 📌 列表的兩種走法：

```python
l = [1, 2, 3]

# 方式 1：用位置一個個印
for i in range(len(l)):
    print(l[i])

# 方式 2：直接走每一個
for element in l:
    print(element)
```

### ✏️ 更改列表裡的東西

```python
l = [1, 2, 3]
l[0] = "A"  # 把第一個改成 A
l[2] = "c"  # 把第三個改成 c
print(l)  # ['A', 2, 'c']
```

---

## 🔗 2. 列表是「指向」還是「複製」？

```python
a = [1, 2, 3]
b = a  # b 跟 a 指向同一個箱子
b[0] = 2
print(a)  # a 也被改了！→ [2, 2, 3]
```

### 🧻 如何做「複製」的版本？

```python
c = [10, 20, 30]
d = c.copy()
d[1] = 200
print(c)  # 原本的沒變
print(d)  # 新的有改

e = c[:]  # 也可以這樣複製
e[2] = 300
print(c)
print(e)
```

---

## 🔧 3. 常見的列表操作

```python
La = [1, 2, 3]
La.append(4)  # 加東西進去
print(La)  # [1, 2, 3, 4]

Lb = ["a", "b", "c", "a"]
Lb.remove("a")  # 移除第一個 "a"
print(Lb)  # ['b', 'c', 'a']

Lc = ["a", "b", "c"]
Lc.pop()  # 把最後一個拿掉
print(Lc)  # ['a', 'b']

Ld = [3, 1, 5, 4, 2]
Ld.sort()  # 排序從小到大
print(Ld)  # [1, 2, 3, 4, 5]

Le = ["apple", "monday", "small", "today"]
Le.sort()  # 字母順序排列
print(Le)
```

---

## 🧱 4. Streamlit 介面小工具（畫面版 Python）

這是一個可以做畫面互動的工具（像點按鈕、輸入文字）

### 🎮 按鈕和欄位

```python
import streamlit as st

st.title("按鈕練習")
col1, col2 = st.columns(2)
col1.button("按鈕 1")
col2.button("按鈕 2")
```

### ⌨️ 文字輸入 & session 狀態記住值

```python
text = st.text_input("請輸入文字")
st.write("你剛剛輸入了：", text)
```

---

## 🍱 5. 點餐機小程式（Streamlit）

🛒 每次輸入一項食物，就可以放進購物籃，再點按鈕刪除

```python
food = col1.text_input("請輸入餐點")
if col2.button("加入"):
    st.session_state.order.append(food)
```

---

## 🔁 6. while 迴圈 & break 中止

```python
i = 0
while i < 10:
    print(i)
    i += 1
```

中途想停下來：

```python
if i == 3:
    break
```

---

## 🎲 7. 隨機數字 & 擲骰子練習

```python
import random

count1 = count2 = count3 = 0
for i in range(30):
    n = random.randrange(1, 4)  # 隨機出 1~3
    if n == 1:
        count1 += 1
    elif n == 2:
        count2 += 1
    else:
        count3 += 1
print(f"1 出現 {count1} 次, 2 出現 {count2} 次, 3 出現 {count3} 次")
```

---

## 🎯 8. 猜數字遊戲

```python
target = random.randint(1, 100)
while True:
    guess = int(input("請猜一個數字："))
    if guess < target:
        print("再大一點")
    elif guess > target:
        print("再小一點")
    else:
        print("你猜對了！")
        break
```

---

## 🎁 9. 一番賞練習（抽抽樂）

抽 1\~100 的號碼，每次花 200 元，看多久中獎！

```python
table = [0] * 100
target = random.randint(1, 100)
table[target - 1] = 1

count = 0
while True:
    pick = random.randint(1, 100)
    if table[pick - 1] == 2:
        print("這格抽過了")
    elif table[pick - 1] == 1:
        print("🎉 恭喜中獎")
        break
    else:
        print("沒中，再抽一次")
        table[pick - 1] = 2
    count += 1
print(f"總共抽了 {count} 次，花了 {count*200} 元")
```

---
