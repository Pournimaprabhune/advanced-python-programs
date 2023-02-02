print("normal thread learning flow of non-daemon thread")
from threading import *
import time
def thread_1():
         for i in range(5):
            print("this is non daemon thread")
            time.sleep(2)

t=Thread(target=thread_1)
t.start()
time.sleep(5)
print("main thread execution")