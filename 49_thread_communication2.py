print("program:inter thread commication by using codition objects in python")
from threading import*
import time
import random

items=[]
def produce(c):
     while True:
        c.acquire()
        item=random.randint(1,10)
        print("producer producing Item:",item)
        items.append(item)
        print("procedure giving notification")
        c.notify()
        c.release()
        time.sleep(5)
def consume(c):
       while True:
           c.acquire()
           print("consumer waiting for updating")
           c.wait()
           print("consumer consumed the item",items.pop())
           c.release()
           time.sleep(5)

c=Condition()
t1=Thread(target=consume,args=(c,))
t2=Thread(target=produce,args=(c,))
t1.start()
t2.start()
