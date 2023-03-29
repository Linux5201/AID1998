"""
进程对象属性
"""

from multiprocessing import Process
import time

def tm():
    for i in range(3):
        time.sleep(2)
        print(time.ctime())


if __name__ == '__main__':
    p = Process(target=tm)
    # p.daemon = True    # 父进程退出子进程也退出
    p.start()
    print("Name:", p.name)   #进程名称
    print("PID:",p.pid)    # 对应子进程PID
    print("is alive:", p.is_alive())   # 判断进程是否在生命周期

    p.join()







