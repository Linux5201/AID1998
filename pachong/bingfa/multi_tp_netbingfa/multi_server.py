"""
multi_server.py

1、创建监听套接字
2、等待接收客户端请求
3、客户端连接，创建新的进程处理客户端请求
4、原进程继续等待其他客户端连接
5、如果客户端退出，则销毁对应的进程
"""
from socket import *
from multiprocessing import Process
import signal
import os

# 全局变量
HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST, PORT)


# 具体处理客户端具体事务
def handle(c):
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b'OK')
    c.close()

if __name__ == '__main__':
    # 创建tcp套接字
    s = socket()
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)     # 设置套接字的端口重用
    s.bind(ADDR)
    s.listen(5)

    # 处理僵尸进程
    # signal.signal(signal.SIGCHLD,signal.SIG_IGN)    # 只能在Linux中使用
    print("listen the port 8888...")

    while True:
        # 循环处理客户端连接
        try:
            c, addr = s.accept()
            print("Connect from",addr)

        except KeyboardInterrupt:
            os._exit(0)
        except Exception as e:
            print(e)
            continue

        # 创建子进程处理客户端事务
        p = Process(target=handle, args=(c,))
        p.daemon = True  # 父进程结束所有服务终止
        p.start()
        c.close()     # 父进程不需要和客户端通信













