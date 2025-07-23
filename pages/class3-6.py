import random

prizeA = int(input("請輸入Ａ賞編號"))

while True:
    guess = int(random.randint(1, 100))
    count = 0
    if prizeA != guess:
        count += 1
    else:
        money = 200 * count
        print(f"你在第{count}抽抽到Ａ賞，共花費{money}元")
        break
