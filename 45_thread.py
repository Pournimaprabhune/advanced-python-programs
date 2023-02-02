import threading
class abc(threading.Thread):
        def __init__(self,name,id):
         threading.Thread.__init__(self)
         self.name=name                 
         self.id=id
        def run(self):
            print(str(self.name)+" "+str(self.id)) 

t1=abc("GFG",1000)
t2=abc("GeeksForGeeks",2000)
t1.start()
t2.start() 
print("Exite")       
