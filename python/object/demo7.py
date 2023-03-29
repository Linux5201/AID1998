"""
    练习：定义对象计数器
    定义老婆类，创建3个老婆对象。
"""

class weif:

    count = 0
    @classmethod
    def Count(cls):
        print(cls.count)

    def __init__(self,name):
        weif.count += 1
        self.name = name

w01 = weif('a')
w02 = weif('b')
w03 = weif('c')



# 可以通过类名访问实例方法，但必须手动传递对象地址,不建议通过类名访问实例方法




