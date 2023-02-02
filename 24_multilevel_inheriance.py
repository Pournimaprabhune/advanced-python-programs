class animal:#base class or parent class
       def speak(self):
         print("animal speaking")

class dog(animal):
                 def bark(self):
                     print("dog barking")
class puppy(dog):
          def eat(self):
            print("Eating bread")

a=puppy()
a.bark() 
a.speak()   
a.eat()                