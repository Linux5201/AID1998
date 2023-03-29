"""
    函数参数
        形式参数
"""
# 1、缺省形参（默认),如果实参不传递，可以使用默认值
def fun01(a = 0,b = 0,c = 0,d = 0):
    print(a)
    print(b)
    print(c)
    print(d)

# 关键字实参 + 缺省实参：调用者可以随意传递参数
fun01(b=2,c=3)

# 练习：定义函数，根据小时，分钟，秒，计算总秒数
# 要求：可以只计算小时-->秒
#      可以只计算分钟-->秒
#      可以只计算小时 + 分钟-->秒
#      可以只计算小时 + 分钟 + 秒-->秒
def fun02(h = 0,m = 0,s = 0):
    sum = h*3600 + m*60 + s
    return sum
print(fun02(h=1,m=1,s=1))

# 2、位置形参
def fun03(a,b,c,d):
    print(a)
    print(b)
    print(c)
    print(d)

# 3、星号元组形参：* 将所有的实参合并为一个元组
# 作用：让实参个数无限 一般将其命名为args
def fun04(*args):
    print(args)

list02 = [1,2,3,4]
fun04(4)
fun04("a")
fun04("a",1)
fun04(list02)

"""
练习：定义函数，数值相加的函数
"""
def sum(*args):
    sum = 0
    for item in args:
        sum += item
    return sum
print(sum(1,2,3,4,5,6,7,8,9))

# 4、命名关键字形参:在星号元组形参以后的位置形参
# 目的：要求实参必须使用关键字实参
def fun05(a,*args,b):
    print(a)
    print(args)
    print(b)
fun05(1,1,b=1)
fun05(1,2,3,b=4)

def fun05(*,a,b):
    print(a)
    print(b)
fun05(a=1,b=2)

# 5、双星号字典形参:实参可以传递数量无限的关键字实参
# ** 目的是将实参合并为字典
def fun06(**a):
    print(a)

fun06(a=1,b=2)

#作业：调用：fun07
def fun07(a,b,*args,c,d,**kwargs):
    print(a)
    print(b)
    print(args)
    print(c)
    print(d)
    print(kwargs)
fun07(1,2,4,5,6,c=7,d=8,e=9,f=10)
