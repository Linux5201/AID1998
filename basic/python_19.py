"""
str list
列表 --->字符串
需求：根据XX逻辑，拼接一个字符串
“0123456789”
"""
result = ""
for item in range(10):
    result += str(item)
print(result)
#缺点：每次循环形成一个新的字符串对象，替换变量引用result


result = list()
for item in range(10):
    result.append(str(item))
result = "".join(result)
print(type(result))
#列表变成字符串
print(result)
result = "-".join(result)
#result = "连接符“.join(列表)
print(result)
#优点：每次循环只向列表添加字符串，没有创建列表对象

#在控制台中循环输入字符串，如果输入空则停止。最后打印所有内容（拼接后的字符串）
str_1 = str(input("输入字符串："))
list02 = list()
while str_1 != "":
    list02.append(str_1)
    str_1 = str(input("输入字符串："))
result = "".join(list02)
print(result)