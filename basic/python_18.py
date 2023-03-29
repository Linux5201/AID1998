"""
练习1：将列表[54,25,12,42,35,17]中，大于30的数字存入另一个列表，并画出内存图，
练习2：在控制台录入5个数字，打印最大值
打印最大值（不适于max）
"""

list01 = [54,25,12,42,35,17]
list02 = list()
for item in range(0,6):
    if list01[item]>30:
        list02.append(list01[item])

list03 = list()
count = 0
while count<5:
    number1 = int(input("输入数字："))
    list03.append(number1)
    count += 1
print(max(list03))
t = list03[0]
for i in list03:
    if t<i:
        t=i
print(t)