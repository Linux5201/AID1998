"""
tcp_client.py   tcp客户端流程
重点代码1
"""

from socket import *

# 创建tcp套接字
sockfd = socket()    # 使用默认参数 -> tcp套接字

# 连接服务器
# server_addr = ('10.16.59.116', 8888)     # 服务端地址
server_addr = ('192.168.1.105', 8888)     # 服务端地址
sockfd.connect(server_addr)

while True:
    # 发送消息
    data = input("Msg>>")
    if not data:
        break
    sockfd.send(data.encode())    # 转换为字节串再发送
    data = sockfd.recv(1024)
    print("Server:", data.decode())    # 打印接收内容


# 关闭套接字
sockfd.close()






