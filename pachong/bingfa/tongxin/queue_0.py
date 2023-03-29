"""
queue_0.py 消息队列演示
注意：消息队列符合先进先出原则
"""
from multiprocessing import Queue,Process
from time import sleep
from random import randint




def handle(q):
    for i in range(6):
        x = randint(1, 34)
        q.put(x)
    q.put(randint(1, 16))

def request(q):
    while True:
        print("摇啊摇.....")
        sleep(2)
        try:
            print(q.get(3))
        except:
            break

if __name__ == '__main__':
    # 创建消息队列
    q = Queue(5)  # 最大长度5
    p1 = Process(target=handle, args=(q,))
    p2 = Process(target=request,args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()





