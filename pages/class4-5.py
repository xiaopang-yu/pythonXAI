import random

result = []


def roll_dice(n):
    i = 0
    while i < n:
        i += 1
        num = random.randint(1, 6)
        result.append(num)
    return result


n = int(input("請輸入投擲次數 "))
outcome = roll_dice(n)
print("投擲結果為", outcome)


count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
count6 = 0

for k in outcome:
    if k == 1:
        count1 += 1
    elif k == 2:
        count2 += 1
    elif k == 3:
        count3 += 1
    elif k == 4:
        count4 += 1
    elif k == 5:
        count5 += 1
    else:
        count6 += 1

print(
    f"1 的次數:{count1}, 2 的次數:{count2}, 3 的次數:{count3}, 4 的次數:{count4}, 5 的次數:{count5}, 6 的次數:{count6}"
)
