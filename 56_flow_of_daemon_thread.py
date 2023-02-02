print("the flow of daemon thread ove non-daemon thread")
from threading import *
import time
def thread_1():
     for i in range(5):
        print("this is thread T")
        time.sleep(3)

t=Thread(target=thread_1)
t.setDaemon(True)
t.start()
time.sleep(5)
print("this is main Thread")