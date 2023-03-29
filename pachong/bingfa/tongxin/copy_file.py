"""
创建两个进程，分别复制文件的上半部分和下半部分到一个新的文件中
"""

from multiprocessing import Process
import os


# 父进程创建fr 两个子进程使用这个fr会相互影响

# 复制上半部分
def top(filename, size):
    fr = open(filename, 'rb')
    fw = open('top.JPG', 'wb')
    n = size // 2
    fw.write(fr.read(n))
    fr.close()
    fw.close()

def bot(filename, size):
    fr = open(filename, 'rb')
    fw = open('bot.JPG', 'wb')
    fr.seek(size // 2, 0)
    fw.write(fr.read())
    fr.close()
    fw.close()

if __name__ == '__main__':
    filename = "E:\DK\Project\learn_torch\pachong\\bingfa\\tongxin\gg.JPG"
    size = os.path.getsize(filename)
    p1 = Process(target=top, args=(filename, size,))
    p2 = Process(target=bot, args=(filename, size,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()





