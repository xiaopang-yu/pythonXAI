print(len([]))
print(["apple"])
print(["a", "b"])
print(len([1, 2, 3]))

l = [1, 2, 3]
for i in range(len(l)):
    print(l[i])

print("-" * 30)

for element in l:
    print(element)

print("-" * 30)

l = [1, 2, 3]
l[0] = "A"
l[2] = "c"
print(l)  # Output: ['A', 2, 'c']

print("-" * 30)


# point
a = [1, 2, 3]
b = a
b[0] = 2
print(a)  # Output: [2, 2, 3]

# 改變是雙向的，a,b指向同一個串列，所以都會變成[2, 2, 3]
# 如果要讓兩個串列是「複製」關係
# a = [1, 2, 3]
# b = a.copy() 或是 b = a[:]

c = [10, 20, 30]
d = c.copy()
d[1] = 200
print(c)  # Output: [10, 20, 30]
print(d)  # Output: [10, 200, 30]
e = c[:]
e[2] = 300
print(c)  # Output: [10, 20, 30]
print(e)  # Output: [10, 20, 300]

print("-" * 30)


La = [1, 2, 3]
La.append(4)
print(La)

Lb = ["a", "b", "c", "a"]
Lb.remove("a")
print(Lb)

Lc = ["a", "b", "c"]
Lc.pop()  # 移除最後的元素，也可以指定位置
print(Lc)

Ld = [3, 1, 5, 4, 2]
Ld.sort()
print(Ld)
