"""
练习：记录一个函数fun01的执行次数
"""
count = 0

def fun01():
    global count
    count += 1

fun01()
fun01()
fun01()
fun01()
fun01()
print("fun01()调用%d次"%count)

