"""
多
行
註
解
"""

# 單行註解

# 全選後 control+? 直接變成多個單行註解
# 要取消就重複動作

print(100)  # 輸出整數
print(0.3124)  # 輸出浮點數
print(True)  # 輸出布林值
print("hello world")  # 輸出字串

a = "hello"
b = "world"
print(a + " " + b)

c = 10
d = 20
print(c + d)  # 輸出兩個整數的和

x = 4
x = x + 3
print(x)  # 輸出變數 x 的值
x = x * 2
print(x)  # 輸出變數 x 的新值

print(7 + 3)
print(7 - 3)
print(7 * 3)
print(7 / 3)  # 除法
print(7 // 3)  # 整數除法
print(7 % 3)  # 取餘數
print(7**3)  # 7 的 3 次方

v1 = 0.1
v2 = 0.2
print(v1 + v2)  # 注意浮點數加法的精度問題

S1 = "hello"
S2 = "world "
S3 = S1 + S2
print(S3)
print(S1 + S2 * 2)

name = "python"
age = 31
new_str = f"我是{name},今年{age}歲"
print(new_str)

print(len(""))  # 輸出字串長度
print(len("hello"))  # 輸出字串長度

print(type(True))  # 輸出布林值類型
print(type(100))  # 輸出整數類型
print(type(123.0))  # 輸出浮點數類型
print(type("hello"))  # 輸出字串類型

print(int(True))
print(int(123))
print(int(123))

print(float(123))
print(float(True))


print(bool(0))
print(bool("hello "))
print(bool(""))  # 空字串是 False
print(bool(" "))  # 空白字串也是

print("開始輸入姓名")
a = input()  # 都是回傳字串型態a
print("輸入的內容是", a)

b = input("輸入年齡資料")
print("您的年齡為", b, "歲")
print(type(b))
b = int(b)
print("兩年後，您的年齡為", b + 2, "歲")


# 題目：向使用者詢問半徑長度，計算出圓面積，並輸出至螢幕
r = float(input("Please enter the radius of the circle :"))
print("The area of the circle is", 3.14 * r**2, "square units")
a = 3.14 * r**2
print("The area of the circle is " + str(a) + " square units")
print(f"The area of the circle is {a} square units")
