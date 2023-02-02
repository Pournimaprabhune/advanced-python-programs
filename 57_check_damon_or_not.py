print("chaeck wether the thread id daemon or not")
from threading import *
print(current_thread().isDaemon())
print(current_thread().daemon)
