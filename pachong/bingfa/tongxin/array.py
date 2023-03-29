"""
array.py
共享内存存放一组数据
"""

from multiprocessing import Process, Array

def fun(shm):
    # array创建共享内存对象可迭代
    for i in shm:
        shm[0] = b'H'    # 修改共享内存
        print(i)

if __name__ == '__main__':
    # shm = Array("i", [1, 2, 3, 4])
    # shm = Array("i", 5)  初始开辟5个整型空间
    shm = Array("c", b'hello')  #字节串
    p = Process(target=fun, args=(shm,))
    p.start()
    p.join()
    for i in shm:
        print(i)

    print(shm.value)    # 打印字节串





