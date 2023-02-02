print("program:inter thread commicationby using evenet objects in python")
from threading import *
import time
def traffic_police():
     #while(10):
        time.sleep(5)
        print("traffic police giveing green signal")
        event.set()
        time.sleep()
        print("traffic police giving RED singnal")
        event.clear()

def driver():
     num=0
     while(10):
       print(" drivers waiting for Green singnal")
       event.set()
       print("traffic signal is green....vehicales can move")
       while event.isSet():
            num=num+1
            print("vehical no:",num,"crossing the singnal")
event=Event()
t1=Thread(target=traffic_police)
t2=Thread(target=driver)
t1.start()
t2.start()


