print("priyority queue wih number")
import queue
q=queue.PriorityQueue()
q.put((1,'Rahun'))
q.put((3,'sharuk'))
q.put((4,'ajay'))
q.put((2,'siva'))
while not q.empty():
    print(q.get()[1])# in above example indexwise first position value will be printed in all tuple
    #print(q.get()[0])# in above example indexwise 0th position value will be printed in all tuple