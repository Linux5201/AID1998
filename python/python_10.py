"""
str编码
"""

#字--->数
# number = ord("a")
# print(number)
#
# char_1 = chr(97)
# print(char_1)

"""
练习1、在控制台获取一个字符串，打印每个字符的编码值
练习2、在控制台中，重复录入一个编码值，然后打印字符,如果输入空字符串，则退出程序

"""
# str_1 = str(input("输入一个字符串:"))
# for item in str_1:
#     print(ord(item))

number_1 = str(input("输入编码值："))
while number_1 != "":
    number_1 = int(number_1)
    char_1 = chr(number_1)
    print(char_1)
    number_1 = str(input("输入编码值："))