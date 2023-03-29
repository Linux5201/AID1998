"""
block_io.py
socket 套接字非阻塞实例
"""

from socket import *
from time import ctime, sleep

# 日志文件
f = open('log.txt', 'a+')



# tcp套接字
sockfd = socket()
sockfd.bind(('127.0.0.1', 8888))
sockfd.listen(3)

# 设置套接字为非阻塞
# sockfd.setblocking(False)

# 非阻塞与超时检测不能一起使用
# 设置超时检测，最多阻塞3秒
sockfd.settimeout(3)

while True:
    print("Wating for connect...")
    # 没有客户端链接每隔3秒写一个日志
    try:
        connfd,addr = sockfd.accept()
    except (BlockingIOError, timeout) as e:
        sleep(3)
        f.write("%s:%s\n"%(ctime(), e))
        f.flush()
    else:
        print("Connect from", addr)
        data = connfd.recv(1024).decode()
        print(data)









