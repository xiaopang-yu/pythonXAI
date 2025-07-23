# 一番賞練習
import random

table = []
for i in range(100):
    table.append(0)

target = random.randint(1, 100)
table[target - 1] = 1  # 要 -1 是因為 table 是 0 到 99 ，target 是 1 到 100

count = 0
while True:
    pick = random.randint(1, 100)
    count += 1
    if table[pick - 1] == 2:
        print("這格已經抽過了")
        count -= 1
    elif table[pick - 1] == 1:
        print("恭喜中獎")
        break
    else:
        print("沒有中獎，請繼續抽")
    table[pick - 1] = 2
print(f"你在第{count}抽抽到Ａ賞，共花費{count*200}元")
