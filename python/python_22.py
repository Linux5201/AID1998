"""

彩票 双色球：
红球：6个，1--33之间的整数 不能重复
篮球：1个，1--16之间的整数
练习1：随机产生一注彩票[6个红球和1个蓝球]

练习2：
”请输入第一个红色球号码："
"号码不在范围内"
"号码已经重复"
"请输入蓝色号码"
"""
number01 = int(input("请输入第一个红色号码："))
list01 = list()
count = 0
while count<1:
    if number01 in range(1,33):
        list01.append(number01)
        count += 1
    else:
        print("号码不在范围内")
        number01 = int(input("请输入第一个红色号码："))

number01 = int(input("请输入第二个红色号码："))
while count<2:
    if number01 in range(1,33) and number01 not in list01:
        list01.append(number01)
        count += 1
    elif number01 in list01:
        print("号码已经重复")
        number01 = int(input("请输入第二个红色号码："))
    elif number01 not in range(1,33):
        print("号码不在范围内")
        number01 = int(input("请输入第二个红色号码："))

number01 = int(input("请输入第三个红色号码："))
while count<3:
    if number01 in range(1,33) and number01 not in list01:
        list01.append(number01)
        count += 1
    elif number01 in list01:
        print("号码已经重复")
        number01 = int(input("请输入第三个红色号码："))
    elif number01 not in range(1,33):
        print("号码不在范围内")
        number01 = int(input("请输入第三个红色号码："))

number01 = int(input("请输入第四个红色号码："))
while count<4:
    if number01 in range(1,33) and number01 not in list01:
        list01.append(number01)
        count += 1
    elif number01 in list01:
        print("号码已经重复")
        number01 = int(input("请输入第四个红色号码："))
    elif number01 not in range(1,33):
        print("号码不在范围内")
        number01 = int(input("请输入第四个红色号码："))

number01 = int(input("请输入第五个红色号码："))
while count<5:
    if number01 in range(1,33) and number01 not in list01:
        list01.append(number01)
        count += 1
    elif number01 in list01:
        print("号码已经重复")
        number01 = int(input("请输入第五个红色号码："))
    elif number01 not in range(1,33):
        print("号码不在范围内")
        number01 = int(input("请输入第五个红色号码："))

number01 = int(input("请输入第六个红色号码："))
while count<6:
    if number01 in range(1,33) and number01 not in list01:
        list01.append(number01)
        count += 1
    elif number01 in list01:
        print("号码已经重复")
        number01 = int(input("请输入第六个红色号码："))
    elif number01 not in range(1,33):
        print("号码不在范围内")
        number01 = int(input("请输入第六个红色号码："))

number01 = int(input("请输入蓝色号码："))
while count<7:
    if number01 in range(1,16):
        list01.append(number01)
        count += 1
    elif number01 not in range(1,33):
        print("号码不在范围内")
        number01 = int(input("请输入蓝色号码："))
print(list01)