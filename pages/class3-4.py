i = 0
while i < 10:
    print(i)
    i = i + 1

print("-" * 30)

i = 0
while i < 5:
    if i == 3:
        break
    print(i)
    i = i + 1

print("-" * 30)

for i in range(5):
    if i == 3:
        break
    print(i)

print("-" * 30)


import random

count1 = 0
count2 = 0
count3 = 0
for i in range(30):
    n = random.randrange(1, 4)  # 只產生 1 到 3 的數，不包含 4
    if n == 1:
        count1 += 1
    elif n == 2:
        count2 += 1
    elif n == 3:
        count3 += 1
    print(n)
print(f"1的次數:{count1},2的次數:{count2},3的次數:{count3}")

print("-" * 30)

print(random.randrange(0, 10, 2))
print(random.randint(10, 20))
