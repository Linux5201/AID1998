"""
Windows下多进程实现

Unix/Linux操作系统提供了一个fork()系统调用，它非常特殊。普通的函数调用，调用一次返回一次，但是fork()调用一次，返回两次，因为
操作系统自动把当前进程（称为父进程）复制了一份（称为子进程），然后，分别在父进程子进程之间返回。
子进程永远返回0，而父进程返回子进程的ID，这样做的理由是，一个父进程可以fork()出很多子进程，所以父进程要记下每个子进程的ID，而子
进程只需要调用getppid()就可以拿到父进程的ID。
Windows操作系统调用multiprocessing.Process也可以达到这种效果
Pool的线程池
注意：每次子程序结束后使用exit(0)退出子程序，不然还会执行程序之外的代码。
"""
from multiprocessing import Pool
import time

def play_music():
    print("开始播放音乐！")
    time.sleep(5)
    print('继续播放下一首音乐！')
    time.sleep(4)
    print('音乐结束！')


def play_game():
    print('游戏开始')
    time.sleep(8)
    print('游戏结束')


def play_move():
    print('视频开始')
    time.sleep(8)
    print('视频结束')



if __name__ == '__main__':
    p = Pool(3)  # 表示同时执行的进程个数
    p.apply_async(play_music)
    p.apply_async(play_game)
    p.apply_async(play_move)
    print("等待所有进程结束")
    p.close()
    p.join()
    print('主程序结束')












