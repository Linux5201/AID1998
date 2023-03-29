


import multiprocessing as mp
from time import sleep


# 进程函数
def fun():
    print("开始第一个进程")
    sleep(5)
    print("子进程结束")



if __name__ == '__main__':
    # 创建进程对象
    p = mp.Process(target=fun)
    p.start()          # 启动进程

    # 父进程事件
    sleep(3)
    print("父进程干点事")
    p.join()           # 回收进程









