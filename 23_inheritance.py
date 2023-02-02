class animal:#base class or parent class
       def speak(self):
         print("animal speaking")

class dog(animal):#(child class or derived class) base class dog inheritse derived class class animal
                 def bark(self):
                     print("dog barking")

a=dog()
a.bark() 
a.speak()                   