from abc import ABC, abstractmethod
class car(ABC):
          @abstractmethod
          def mileage(self):
              pass
class toyota(car):
         def mileage(self):
              print("the mileage of toyota is 35 kmph")
class suzuki(car):
        def mileage(self):
              print("the mileage of toyota is 25 kmph")
class  duster(car):         
    def mileage(self):
              print("the mileage of toyota is 27 kmph")
class renualt(car):           
     def mileage(self):
              print("the mileage of toyota is 28 kmph")         

t=toyota()
t.mileage()
s=suzuki()
s.mileage()
d=duster()
d.mileage()
r=renualt()
r.mileage()

