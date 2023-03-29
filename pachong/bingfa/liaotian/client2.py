"""
chat room 客户端
发送请求，展示结果
"""

import multiprocessing as mp
from socket import *
import os, sys


# 服务器地址
ADDR = ('192.168.1.105', 8888)

# 发送消息
def send_msg(s, name):
    while True:
        text = input("发言：")
        msg = "C %s " \
              "%s"%(name, text)
        s.sendto(msg.encode(), ADDR)

# 接收消息
def recv_msg(s):
    while True:
        data, addr = s.recvfrom(4096)
        print(data.decode())


# 客户端启动函数
def main():
    s = socket(AF_INET, SOCK_DGRAM)

    # 进入聊天室
    while True:
        name = input("请输入姓名：")
        msg = 'L ' + name
        s.sendto(msg.encode(), ADDR)
        data,addr = s.recvfrom(128)
        if data.decode() == 'OK':
            print("您已进入聊天室")
        else:
            print(data.decode())
        # 已经进入聊天室

        p = mp.Process(target=recv_msg,args=(s,))
        send_msg(s,name)
        p.start()
        p.join()




main()




