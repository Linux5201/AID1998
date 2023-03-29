from time import sleep
from threading import Thread, Lock


# 交易类
class Account:
    def __init__(self, id, balance, lock):
        self.id = id   # 用户
        self.blance = balance   # 存款
        self.lock = lock   # 锁


    # 取钱
    def withdraw(self,amount):
        self.blance -= amount

    # 存钱
    def deposit(self, amount):
        self.blance += amount

    # 查看余额
    def get_balance(self):
        return self.blance

def transfer(from_, to, amount):
    if from_.lock.acquire():  # 锁住自己账户
        from_.withdraw(amount)  # 账户减少
        sleep(0.5)
        if to.lock.acquire():  # 对方账户上锁
            to.deposit(amount)  # to账户加钱
            to.lock.release()  # to解锁

        from_.lock.release()  # from账户解锁
    print("%s给%s转账%d" % (from_.id, to.id, amount))




if __name__ == '__main__':
    # 产生账号
    Tom = Account('Tom', 5000, Lock())
    Alex = Account('Alex', 8000, Lock())
    t1 = Thread(target=transfer,args=(Tom, Alex, 2000))
    t2 = Thread(target=transfer, args=(Alex, Tom, 3500))
    t2.start()
    t1.start()
    t1.join()
    t2.join()





























