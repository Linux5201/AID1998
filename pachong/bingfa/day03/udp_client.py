"""
udp_client.py udp客户端流程
重点代码

服务端提供逻辑和数据处理
发送端发送请求和展现请求结果
"""

from socket import *

# 服务器地址
ADDR = ('127.0.0.1', 8888)


# 创建套接字
sockfd = socket(AF_INET, SOCK_DGRAM)

# 循环收发消息
while True:
    data = input("Msg>>")
    if not data:
        break
    sockfd.sendto(data.encode(), ADDR)
    msg, addr = sockfd.recvfrom(1024)
    print("From server：", msg.decode())

# 关闭套接字
sockfd.close()








