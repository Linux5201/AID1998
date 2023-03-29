"""
event 线程互斥方法演示
"""

from threading import Thread, Event

s = None  # 用于通信
e = Event()   # 事件对象

def Yangzirong():
    print("杨子荣前来拜山头")
    global s
    s = "天王盖地虎"
    e.set()    # 操作完共享资源 e 设置


if __name__ == '__main__':
    t = Thread(target=Yangzirong)
    t.start()
    print("说对口令就是自己人")
    e.wait()    # 阻塞等待
    if s == '天王盖地虎':
        print('宝塔镇河妖')
        print("口令正确")
    else:
        print("打死他")

    t.join()



















