"""
进程池使用实例
"""

from multiprocessing import Pool
from time import sleep,ctime


# 进程池事件
def work(msg):
    sleep(2)
    print(ctime(),'--',msg)


if __name__ == '__main__':
    # 创建进程池
    pool = Pool()

    # 向进程池队列添加事件
    for i in range(10):
        msg = "Tedu %d"%i
        pool.apply_async(func=work,args=(msg,))

    # 关闭进程池
    pool.close()

    # 回收进程池
    pool.join()









