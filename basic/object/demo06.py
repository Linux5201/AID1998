"""
    类成员
    类变量
    1、语法
        （1）定义：在类中，方法外定义变量。
        class 类名：
            变量名 = 表达式
        （2）调用：类名.变量名
                 不建议通过对象访问类变量
    2、说明
        ——存储在类中。
        ——只有一份，被所有对象共享。
    3、作用：描述所有对象的共有数据
    类方法
    1、语法
        （1）定义：
        @classmethod
        def 方法名称（cls.参数列表）：
        方法体
        （2）调用：类名.方法名（参数列表）
        不建议通过对象访问类方法
    2、说明
    ——至少有一个形参，第一个形参用于绑定类，一般命名为‘cls'
    ——使用@classmethod修饰的目的是调用类方法时可以隐式传递类。
    ——类方法中不能访问实例成员，实例方法中可以访问类成员。

"""
class ICBC:
    """
    工商银行
    """
    # 表示总行的钱
    total_money = 1000000
    # 因为类方法没有对象地址self，所以不能访问实例成员
    @classmethod
    def print_total_money(cls):
        print("总行还剩%d钱"%cls.total_money)

    def __init__(self,name,money):
        self.name = name
        self.money = money
        # 表示从总行中扣除当前支行使用的金额
        ICBC.total_money -= money

i01 = ICBC("广渠门支行",100000)
i01 = ICBC("陶然亭支行",100000)
print("总行还剩%d钱"%ICBC.total_money)

# 通过类名访问类方法，会将类名传入类方法
ICBC.print_total_money()





