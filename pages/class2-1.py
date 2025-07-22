# # 比較運算子

# print(1 == 2)
# print(1 != 2)
# print(1 >= 2)
# print(1 <= 2)
# print(1 > 2)
# print(1 < 2)


# # 邏輯運算子

# print(not True)
# print(not False)
# print(False and False)
# print(False and True)
# print(True and False)
# print(True and True)

# print(False or False)
# print(False or True)
# print(True or False)
# print(True or True)


# #practice：密碼驗證
# password = input("請輸入密碼：")
# if password == "0427":
#     print("歡迎媽咪回家")
# elif password == "0713":
#     print("歡迎把拔回家")
# elif password == "1102":
#     print("歡迎胖胖回家")
# else:
#     print("密碼錯誤，請重新輸入")


# # 題目：判斷閏年

# year = int(input("請輸入年份"))
# if year % 400 == 0:
#     result = "是"
# elif year % 100 == 0:
#     result = "不是"
# elif year % 4 == 0:
#     result = "是"
# else:
#     result = "不是"
# print(year, "年", result, "閏年")


# #題目：判斷閏年寫法二

# year = int(input("請輸入年份"))
# if year % 4 == 0 :
#     if year % 100 == 0 :
#         if year % 400 == 0 :
#             result = "是"
#         else:
#             result = "不是"
#     else:
#         result = "是"
# else:
#     result = "不是"
# print(year, "年", result, "閏年")


# #題目：判斷閏年寫法三
# year = int(input("請輸入年份"))
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     result = "是"
# else:
#     result = "不是"
# print(year, "年", result, "閏年")
