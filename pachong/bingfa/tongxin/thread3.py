"""
thread3.py
创建步骤
1、继承Thread类
2、重新_init_方法添加自己的属性，使用super加载父类属性
3、重新run方法
使用方法
1、实例化对象
2、调用star自动执行run方法
3、调用join回收线程
"""

"""
自定义线程类
"""

from threading import Thread
from time import sleep, ctime


class MyThread(Thread):
    def __init__(self, target=None, args=(), kwargs={}):
        super().__init__()
        self.target = target
        self.args = args
        self.kwargs = kwargs

    def run(self):
        self.target(*self.args, **self.kwargs)


def player(song, sec):
    for i in range(3):
        sleep(sec)
        print('Playing %s : %s' % (song, ctime()))

if __name__ == '__main__':
    t = MyThread(target=player, args=('葫芦娃', 2))
    t.start()
    for i in range(3):
        sleep(2)
        print('Playing %s : %s' % ('哪吒', ctime()))
    t.join()











