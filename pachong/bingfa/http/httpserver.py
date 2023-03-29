"""
httpserver v1.0
基本要求： 1、获取来自浏览器的请求
         2、判断如果请求内容是/ 将index.html返回给客户端
         3、如果请求的是其他内容则返回404
"""
import socket
from socket import *


# 客户端（浏览器）处理
def request(connfd):
    # 获取请求，将请求内容提取出来

    data = connfd.recv(4096)
    request_line = data.decode().split('\n')[0]
    info = request_line.split(' ')[1]

    # 判断是/ 则返回index.html 不是则返回404
    if info == '/':
        with open('index.html') as f:
            response = "HTTP/1.1 200 OK\r\n"
            response += "Content-Type:text/html\r\n"
            response += "\r\n"
            response += f.read()
    else:
        response = "HTTP/1.1 404 Not Found\r\n"
        response += "Content-Type:text/html\r\n"
        response += "\r\n"
        response += "<h1>Sorry...</h1>"
    # 发送给浏览器
    connfd.send(response.encode())


# 搭建tcp网络
sockfd = socket()
sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)   # 设置端口重用
"""
假如端口被socket使用过，并且利用socket.close来关闭连接，但此时端口还没有释放，要经过
一个TIME_WAIT的过程之后才能使用，为了实现端口的马上复用，可以选择setsockopt()来达到目的。
"""
sockfd.bind(('0.0.0.0', 8000))
sockfd.listen(3)
while True:
    connfd, addr = sockfd.accept()
    request(connfd)    # 处理客户端请求

# connfd.close
# socket.close()











