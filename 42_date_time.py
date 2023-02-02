import time
#prints the number of ticks spent sice 12am 1st january 1970
print(time.time())
#returns a time tuple
print(time.localtime(time.time()))
#returns the formattted time
print(time.asctime(time.localtime(time.time())))
for i in range(0,5):
          print(i)
          time.sleep(1)#each element will be printed after 1 second
          