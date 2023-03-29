"""
ftp 文件服务器，服务端
env:python3.6
多进程/线程并发 socket
"""
import sys
import os
from socket import *
from threading import Thread
import time

# 全局变量
HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST, PORT)
FTP = "E:\DK\Project\learn_torch\pachong\\bingfa\multi_tp_netbingfa\\ftp\\"  # 文件库位置  使用绝对路径

# 创建类实现服务器文件处理功能
class FTPServer(Thread):
    """
    查看列表，下载，上传，退出处理
    """
    def __init__(self, connfd):   # 重写init
        self.connfd = connfd
        super().__init__()    # 加载父类当中的属性


    def do_list(self):
        # 获取文件列表
        files = os.listdir(FTP)
        if not files:
            self.connfd.send("文件库为空".encode())
            return
        else:
            self.connfd.send(b'OK')
            time.sleep(0.1)
        # 拼接字符
        filelist = ""
        for file in files:
            if file[0] != '.' and os.path.isfile(FTP+file):   # 判断文件是否是隐藏文件以及是否是普通文件
                filelist += file + '\n'
        self.connfd.send(filelist.encode())

    def do_get(self, filename):
        try:
            f = open(FTP+filename, 'rb')
        except Exception:
            # 打开失败文件不存在
            self.connfd.send('文件不存在'.encode())
            return
        else:
            self.connfd.send(b'OK')
            time.sleep(0.1)
        # 发送文件
        while True:
            data = f.read(1024)
            if not data:
                time.sleep(0.1)
                self.connfd.send(b'##')
                break
            self.connfd.send(data)

    def do_put(self, filename):
        if os.path.exists(FTP + filename):
            self.connfd.send('文件已存在'.encode())
            return
        else:
            self.connfd.send(b'OK')
        f = open(FTP+filename, 'wb')
        # 循环接收写入文件
        while True:
            data = self.connfd.recv(1024)
            if data == b'##':  # 发送完成
                break
            f.write(data)
        f.close()



    # 循环接收请求，分情况调用功能函数
    def run(self):
        while True:
            data = self.connfd.recv(1024).decode()
            if data == 'Q' or not data:
                return   # 线程结束
            elif data == 'L':
                self.do_list()
            elif data[0] == 'G':
                filename = data.split(' ')[-1]
                self.do_get(filename)
            elif data[0] == 'P':
                filename = data.split(' ')[-1]
                self.do_put(filename)






# 搭建网络服务端模型
def main():
    # 创建tcp套接字
    sockfd = socket()

    # 绑定地址
    sockfd.bind(('0.0.0.0', 8888))

    # 设置监听
    sockfd.listen(5)
    while True:
        # 阻塞等待处理连接
        print("Waiting for connect...")
        try:
            connfd, addr = sockfd.accept()
            print("Connect from", addr)  # 打印链接的客户端地址
        except KeyboardInterrupt:
            print("Server exit")
            break
        except Exception as e:
            print(e)
            continue

        t = FTPServer(connfd)
        t.setDaemon(True)
        t.start()






if __name__ == '__main__':
    main()
