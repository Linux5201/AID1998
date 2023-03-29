"""
练习1：在控制台录入，西游记中你喜欢的人物
输入空字符串，打印所有人物
"""
characher = str(input("输入西游记中的人物："))
list01 = []
while characher != "":
    list01.append(characher)
    characher = str(input("输入西游记中的人物："))
print(list01)
for item in list01:
    print(item)