"""
multiprocessing 创建多个进程


1、使用multiprocessing创建进程同样是子进程复制父进程空间代码，父子进程运行互不影响。
2、子进程只运行target绑定的函数部分。
3、multiprocessing中父进程往往只用来创建子进程，回收子进程，具体事件由子进程完成。
4、multiprocessing创建的子进程中无法使用标准输入
"""

from multiprocessing import Process
from time import sleep
import os

def th1():
    sleep(3)
    print("吃饭")
    print(os.getppid(),'--',os.getpid())

def th2():
    sleep(2)
    print("睡觉")
    print(os.getppid(),'--',os.getpid())

def th3():
    sleep(4)
    print("打豆豆")
    print(os.getppid(), '--', os.getpid())




if __name__ == '__main__':
    things = [th1, th2, th3]
    jobs = []
    for th in things:
        p = Process(target=th)
        jobs.append(p)     # 通过列表将进程对象保存
        p.start()


    # 一起回收
    for i in jobs:
        i.join()





