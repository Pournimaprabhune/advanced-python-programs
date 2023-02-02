class animal:
       def speak(self):
         print("animal speaking")

class dog(animal):
        def speak(self):#method overinding
          print("dog barking")

a=dog() 
a.speak()                    