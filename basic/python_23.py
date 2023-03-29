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
list01 = []

while len(list01)<6:
    number = int(input("请输入第%d个红色号码：" % (len(list01)+1)))
    if number<1 or number>33:
        print("号码不在范围内")
    elif number in list01:
        print("号码已经重复")
    else:
        list01.append(number)
while len(list01)<7:
    number = int(input("请输入蓝色号码："))
    if number<1 or number>16:
        print("号码不在范围内")
    else:
        list01.append(number)
print(list01)