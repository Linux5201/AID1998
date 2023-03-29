"""
for语句，用来遍历可迭代对象的数据元素。
可迭代对象是指依次获取元素的对象

语法：
for 变量列表 in 可迭代对象
    语句块
"""
str01 = "我叫苏大强！"
# item存储的是字符串中每个字符的地址
for item in str01:
    print(item)

#整数生成器：range(开始值，结束值，步长）顾前不顾后
#for + range ：更善于执行预定次数
for item in range(5):
    print(item)

thickness = 0.0001
for item in range(10):
    thickness += 2
print(thickness)
"""
for:适合执行预定次数
while:适合根据条件循环
练习1：累加1--100的和1+2+.....+100
练习2：累加1--100的偶数和2+4+6+.........+100
练习3：累加10--36之间的和
"""

item_1 = 1
sum_1=0
for i in range(1,101):
    sum_1+=item_1
    item_1+=1
print(sum_1)

item_2 = 2
sum_2=0
for i in range(2,101,2):
    sum_2+=item_2
    item_2+=2
print(sum_2)

item_3 = 10
sum_3 = 0
for i in range(10,37):
    sum_3+=item_3
    item_3+=1
print(sum_3)