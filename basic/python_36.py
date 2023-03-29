"""
集合
1、创建一个集合
set01 = set()
set01 = set("abcac")
str01 = str(set01)
print(str01)

2、添加元素
"""
set01 = set()
set01 = set("abcac")
str01 = list(set01)
result = "-".join(str01)  #列表转字符串
result1 = result.split("-") #字符串转列表
print(result1)
print(type(result1))
print(type(result))
print(result)

#添加元素
set02 = {"a","b","a"}
set02.add("qtx")
print(set02)

#删除元素
set02.remove("a")
print(set02)

#获取所有元素
for item in set02:
    print(item)

#数学运算：交集、并集、补集、子集、超集
set01 = {1,2,3}
set02 = {2,3,4}
print(set01 & set02) #交集
print(set01 | set02) #并集
print(set01 ^ set02) #补集
#子集
set03 = {1,2}
print(set03 < set01)
#超集
print(set01 > set03)

#练习1：在控制台中录入字符串，输入空字符停止
#      打印所有不重复的文字
"""
练习2：经理：曹操、刘备、孙权
      技术：曹操，刘备、张飞、关羽
请计算：
      （1）是经理也是技术的有谁？
      （2）是经理不是技术的有谁？
      （3）是技术，不是经理的有谁？
      （4）张飞是经理吗？
      （5）身兼一职的有谁？
      （6）经理和技术总共有多少人？
"""
list_str = []
set_str = set()
# list_str = input("请输入字符串：")
# for item in list_str:
#     set_str.add(item)
# result01 = list(set_str)
# print(result01)
# result01 = "".join(result01)
# print(result01)
while True:
    str = input("请输入字符串：")
    if str == "":
        break
    list_str.append(str)
set_str = set(list_str)
print(set_str)
result01 = list(set_str)
print(result01)
result01 = " ".join(result01)
print(result01)
# result02 = result01.split(" ")
# print(result02)










