"""

列表推导式
练习：将list01中所有元素，增加1以后存入list02中
使用简易方法，将可迭代对象转换为列表
语法： 变量 = [表达式 for 变量 in 可迭代对象]
      变量 = [表达式 for 变量 in 可迭代对象 if 条件]
"""

list01 = [5,56,6,7,8,9]
# list02 = []
# for item in list01:
#     list02.append(item+1)
# print(list02)

list02 = [item + 1 for item in list01]
print(list02)

#将list01中大于10元素，增加1后存入list03中
list03 = [item for item in list01 if item>10]
print(list03)
