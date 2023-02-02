class birds:
     def intro1(self):
         print("there are multiple types of birds in the world")
     def flight1(self):
         print("many of these birds can fly and cannot")
class sparrow1(birds):
     def flight1(self):
         print("sparrow are birds which can fly")
class ostrich(birds):
       def fligt1(self):
         print("ostrich are the birds which cannot fly")

obj1=birds()
obj2=sparrow1()
obj3=ostrich()

obj1.intro1()
obj1.flight1()

obj2.intro1()
obj2.flight1()

obj3.intro1()
obj3.flight1()



