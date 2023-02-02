print("change main to daemon thread")
from threading import *
print(current_thread().setDaemon(True))