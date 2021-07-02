from threading import Thread,Lock
import time


# def counter():
#     for i in range (10):
#         print(i)
#         time.sleep(1)

# def main():
#     t1=Thread(target=counter)
#     t1.start()
#     t2=Thread(target=counter)
#     t2.start()
#     t1.join()
#     t2.join()


class Account():
    def __init__(self) -> None:
        self._lock=Lock()
        self._balance=0
    def deposit(self,money):
        self._lock.acquire()
        try:
            new_balance=self._balance+money
            time.sleep(0.01)
            self._balance=new_balance
        finally:
            self._lock.release()

    @property
    def balance(self):
        return self._balance
    
class AddMoneyThred(Thread):
    def __init__(self,account,money):
        super(  ).__init__()
        self._account=account
        self._money=money
    def run(self):
        self._account.deposit(self._money)
    
def main():
    account=Account()
    threads=[]
    for _ in range(100):
        t= AddMoneyThred(account,1)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print(account.balance)


class read(Thread):
    def __init__(self):
        super().__init__(self)