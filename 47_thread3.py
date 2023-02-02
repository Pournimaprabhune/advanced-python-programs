import threading 
import time 
class abc(threading.Thread):
    def __init__(self,name,counter):
       threading.Thread.__init__(self)
       #self.id=id
       self.name=name
       self.counter=counter
    def run(self):
        print("starting"+self.name)
        threadLock.acquire()
        print_time(self.name,self.counter,3)
        threadLock.release()
        
def print_time(name,delay,counter):
    while counter:
        time.sleep(delay)
        print("%s:%s"%(name,time.ctime(time.time())))
        counter-=1
        
threadLock=threading.Lock()         
t1=abc("Thread1",1)
t2=abc("Thread2",2)
t1.start()
t2.start()
print("EXIT")
