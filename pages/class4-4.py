def hello():
    print("hello")


def hello_2(name):
    print("hello " + name)


def my_max(a, b):
    if a > b:
        return a
    else:
        return b


def calculate_circle_area(r, pi=3.14, scale=1):
    return r**2 * pi


hello()
hello_2("Mike")
ans = my_max(10, 28)
print(my_max(1, 20))

print(calculate_circle_area(10))
print(calculate_circle_area(10, scale=2))
print(calculate_circle_area(10, 3.14159, 5))

print("-" * 30)

length = 5
area = 123


def calculate_square_area():
    # print("面積是", area)  ＃會報錯
    area = length**2
    print("面積是", area)


def calculate_square_area_2():
    area = length**2
    return area


def calculate_square_area_3():
    global area
    area = length**2


length = 10
calculate_square_area()
print(calculate_square_area_2())
calculate_square_area_3()
print(area)


# practice

dis = 0


def distance(x1, y1, x2, y2):
    dis = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return dis


print("請輸入兩個點的座標")
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

print(distance(x1, y1, x2, y2))
