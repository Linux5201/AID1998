"""
Process 给进程函数传参
"""

from multiprocessing import Process
from time import sleep

# 带参数的进程函数
def worker(sec, name):
    for i in range(3):
        sleep(sec)
        print("I'm %s"%name)
        print("I'm working..")

if __name__ == '__main__':
    p = Process(target=worker,args=(2,'Baron'))

    p.start()
    p.join()








