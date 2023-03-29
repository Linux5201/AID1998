import select
import socket
import queue

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 服务端套接字
s.setblocking(0)  # 非阻塞

s.bind(('127.0.0.1', 8000))  # 绑定可用ip端口
s.listen(5)  # 监听套接字

in_ = [s]  # 待监听的可读队列
'''
s的可读行为: 有新的链接
客户端套接字行为: 有数据发来
'''
out_ = []  # 可写队列，发送消息

msg_queue = {}

while in_:
    print('等待下一次事件...')
    readable, writable, exceptional = select.select(in_, out_, in_)
    for socket_ in readable:  # 监听可读队列
        if socket_ is s:  # 当前套接字为服务端套接字，相应的可读事件为有用户链接来
            c, c_addr = s.accept()
            print('有新的套接字连接')
            c.setblocking(0)  # 新连接的客户端套接字设置为非阻塞
            in_.append(c)  # 加入可读监听队列中
            msg_queue[c] = queue.Queue()  # 为当前客户端放置消息存放队列
        else:  # 非服务端套接字，客户端套接字可读事件为有消息发来
            data = socket_.recv(1024)  # 接收客户端数据
            if data == '':  # 客户端断开连接
                print('套接字关闭...[%s]' % socket_)
                if socket_ in out_:
                    out_.remove(socket_)
                in_.remove(socket_)  # 在两个监听队列里删除
                socket_.close()
            else:  # 有客户端消息发来
                msg_queue[socket_].put(data)  # 放置数据到该客户端的消息队列中
                if socket_ not in out_:  # 放置监听套接字到可写事件队列中
                    out_.append(socket_)

    for socket_ in writable:
        try:
            q = msg_queue.get(socket_)  # 获取当前是否含有消息队列，待群发消息
            if q:  # 如果存在
                if q.empty():  # 无消息 踢出队列
                    out_.remove(socket_)
                else:
                    send_data = q.get_nowait()  # 取出消息
        except:
            out_.remove(socket_)
        else:
            for s_ in in_:
                if s_ is not s:  # 不是服务端套接字
                    try:
                        s_.send(send_data)
                    except:
                        in_.remove(s_)
                        if s_ in out_:
                            out_.remove(s_)
                        s_.close()
