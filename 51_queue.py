print("FIFO queue")
import queue
q=queue.Queue()
q.put(10)
q.put(5)
q.put(20)
q.put(15)
while not q.empty():
    print(q.get())