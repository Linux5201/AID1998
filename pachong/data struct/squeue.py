"""
squeue.py 队列的顺序存储

思路分析：
1、基于列表完成数据存储
2、通过封装规定数据操作
3、先确定列表哪一端作为队头
"""
# 自定义队列异常
class QueueError(Exception):
    pass

# 队列操作
class SQueue:
    # 初始化
    def __init__(self):
        self.queuue = []

    # 判断队列是否为空
    def is_empty(self):
        return self.queuue == []

    # 入队
    def enqueue(self, val):
        self.queuue.append(val)

    # 出队
    def dequeue(self):
        if not self.queuue:
            raise QueueError("Queue is empty")

        return self.queuue.pop(0)

if __name__ == "__main__":
    sq = SQueue()
    for i in range(10):
        sq.enqueue(i)

    from sstack import *
    st = SStack()
    while not sq.is_empty():
        st.push(sq.dequeue())
    while not st.is_empty():
        sq.enqueue(st.pop())


    while not sq.is_empty():
        print(sq.dequeue())









