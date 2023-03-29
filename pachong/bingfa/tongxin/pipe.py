"""
pipe.py 管道通信
注意：1、multiprocessing中管道通信只能用于有
        亲缘关系进程中
     2、管道对象在父进程中创建，子进程通过父进程获取
"""
from multiprocessing import Process,Pipe



def app1(fd1):

    print("启动app1,请登录")
    print("请求app2 授权")
    fd1.send("app1 请求登录")      # 写入管道
    data = fd1.recv()
    if data:
        print("登录成功：", data)


def app2(fd2):

    data = fd2.recv()   # 阻塞等待读取管道内容
    print(data)
    fd2.send(('Dave', '123'))



if __name__ == '__main__':
    # 创建管道
    fd1, fd2 = Pipe()
    p1 = Process(target=app1, args=(fd1,))
    p2 = Process(target=app2, args=(fd2,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()









