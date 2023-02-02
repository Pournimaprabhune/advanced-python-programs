print("one interface and two subclasses to that interface")
from abc import *
class DBinterface(ABC):
        @abstractmethod
        def connect(self):
          pass
        @abstractmethod
        def  disconnect(self):
            pass
class orcle(DBinterface):
         def connect(self):
            print("oracle database is coneected")
         def disconnect(self):
            print("oracle database is disconnected")
class sybase(DBinterface):
         def connect(self):
            print(" sybase database is coneected")
         def disconnect(self):
            print(" sybase database is disconnected")
dbname=input("enter the  database name either oracle or sybase databse:")
classname=globals()[dbname]
x=classname()
x.connect()
x.disconnect()
