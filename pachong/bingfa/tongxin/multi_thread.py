"""
效率测试：
Single cpu: 9.974254131317139
Single cpu: 16.376121759414673
"""
from threading import Thread
import time
from test import *




if __name__ == '__main__':
    jobs = []
    tm = time.time()

    for i in range(10):
        t = Thread(target=io)
        jobs.append(t)
        t.start()
    for i in range(10):
        jobs[i].join()

    print("Single cpu:", time.time() - tm)



















