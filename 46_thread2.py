from threading import Thread
from time import sleep
def threaded_function(args):
    for i in range(args):
         print("running")
         sleep(1)
if __name__=="__main__":
     t=Thread(target=threaded_function,args=(10,))
     t.start()
     t.join()
print("thread finished exiting")          
