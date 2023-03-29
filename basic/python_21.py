"""

彩票 双色球：
红球：6个，1--33之间的整数 不能重复
篮球：1个，1--16之间的整数
练习1：随机产生一注彩票[6个红球和1个蓝球]

"""

import random
number01 = random.randint(1,33)
list01 = list()
count = 0
while count<6:
    if number01 not in list01:
        list01.append(number01)
        count += 1
    number01 = random.randint(1, 33)
number01 = random.randint(1,16)
list01.append(number01)
print(list01)


