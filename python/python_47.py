"""
作用域：LEGB
1、作用域：变量起作用的范围
2、Local局部作用域：函数内部
3、Enclosing 外部嵌套作用域：函数嵌套
4、Global全局作用域：模块（.py文件）内部
5、Builtin内置模块作用域：builtins.py文件
"""
#全局变量
g01 = "ok"


def fun01():
    """
    局部作用域（局部变量）在函数内部定义的变量
    :return:
    """
    #在函数中可以读取全局变量,如果想要改全局变量，可以通过global，定义全局变量
    global g01
    l01 = 100
    #创建了一个局部变量g01,而不是修改全局变量
    g01 = "no"
    global g02
    g02 = 250
    print(l01)
    print(g01)
fun01()
print(g02)









