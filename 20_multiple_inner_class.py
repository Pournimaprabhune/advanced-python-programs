class doctors:
     def __init__(self):
        self.name="doctor"
        self.den=self.denstist()
        self.car=self.cardiologist()
     def show(self):
          print("in outer class")
          print("name:",self.name)

     class denstist:

        def __init__(self):
         self.name="dr savita"
         self.degree="BDS"
        def display(self):
          print("name:",self.name)
          print("degree :",self.degree)

     class cardiologist:
             def __init__(self):
                  self.name="dr amit"
                  self.degree="MBBS"
             def display(self):
                 print("name:",self.name)
                 print("degree :",self.degree)
outer=doctors()
outer.show()
d1=outer.den
d2=outer.car
print("\n")
d1.display()
print()
d2.display()
