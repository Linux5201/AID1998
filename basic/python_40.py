"""
自定义函数
定义：
1、用于封装一个特定的功能，表示一个功能或者行为。
2、函数可以重复执行的语句块，可以重复调用
作用：
提高代码的可重用性和可维护性（代码层次结构更清晰）
3、定义函数
1、语法：
def 函数名（形式参数）：
    函数体
2、说明：
def 关键字：全称是define,意为定义
函数名:对函数中语句的描述，
"""
#形式参数
def attack_repeat(count):
    """
    :param count: 攻击次数，int类型
    :return:
    """
    for i in range(count):
        print("临门一脚")
        print("直拳")
        print("摆拳")
        print("肘击")


attack_repeat(3)
attack_repeat(5)