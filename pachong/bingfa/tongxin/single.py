"""
效率测试：
Single cpu: 10.130166292190552
Single IO: 15.376971960067749

"""

from test import *
import time
from multiprocessing import process




if __name__ == '__main__':
    tm = time.time()
    for i in range(10):
        io()
        # count(1, 1)

    print("Single IO:",time.time() - tm)














