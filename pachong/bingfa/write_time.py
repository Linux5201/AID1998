"""
每行写入一个时间
"""


import time

f = open('log.txt', 'a+', 1)

f.seek(0,0)
n=0


for line in f:
    n += 1

while True:
    time.sleep(1)
    n = n + 1
    s = "%d. %s\n"%(n, time.ctime())
    f.write(s)








