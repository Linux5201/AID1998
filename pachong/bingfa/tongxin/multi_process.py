"""
效率测试：
Single cpu: 5.794288396835327
Single IO: 8.536417007446289
"""

from test import *
from multiprocessing import Process
import time



if __name__ == '__main__':
    jobs = []

    tm = time.time()
    for i in range(10):
        p = Process(target=io)

        jobs.append(p)
        p.start()

    for i in range(10):
        jobs[i].join()

    print("Single IO:", time.time() - tm)








