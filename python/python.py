"""
练习：随机加法考试
"""
import random

# number_one = random.randint(1,10)
# number_two = random.randint(1,10)

count = 0
score = 0
while count<3:
    number_one = random.randint(1, 10)
    number_two = random.randint(1, 10)
    number_three = int(input("请输入"+str(number_one)+"+"+str(number_two)+"="+"? "))
    if number_three == number_one + number_two:
        score+=10
    count+=1
print("总分："+str(score))
