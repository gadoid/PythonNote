from threading import Thread,Lock
import threading
class check(Thread):
    def __init__(self):
        super().__init__()
    
    def run(self):
        n=0
        while n < 10 : 
            print(n)
            n+=1

list=[]
for _ in range(4):
    _=check()
    list.append(_)
for i in list :
    i.start()
    i.join