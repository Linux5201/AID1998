
"""
猜数字游戏
游戏运行产生一个1--100之间的随机数，让玩家重复猜测，直到猜对为止
"""
import random
random_number = random.randint(1,100)
print(random_number)
number_one = int(input("输入一个数字："))
while number_one != random_number:
    if number_one>random_number:
        number_one = int(input("你猜大了！重新输入一个数字："))
    elif number_one<random_number:
        number_one = int(input("你猜小了！重新输入一个数字："))
print("你猜对了！")