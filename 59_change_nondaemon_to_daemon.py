print("change non daemon to daemon")
from threading import*
def fun():
    print("Geeks For Geeks")

t=Thread(target=fun)
print("GFG")
print(t.isDaemon())

#set Thread as Daemon
t.setDaemon(True)

#check status
print(t.isDaemon())
t.start()