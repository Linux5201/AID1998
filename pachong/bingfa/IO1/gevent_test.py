import gevent
from gevent import monkey
monkey.patch_time()
from time import sleep   # 在time导入之前导入monkey

# 协程函数
def foo(a, b):
    print("Running foo", a, b)
    gevent.sleep(2)
    print("Foo again..")

def bar():
    print("Running bar")
    gevent.sleep(3)
    print("Bar again..")


# 生成协程对象
f = gevent.spawn(foo, 1, 2)
b = gevent.spawn(bar)
gevent.joinall([f, b])   # 阻塞等待f,b执行完毕















