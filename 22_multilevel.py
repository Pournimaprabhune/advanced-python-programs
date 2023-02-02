class abc:
     def __init__(self):
        self.inner1=self.inner()
     def show(self):
        print("this is outer class")

     class inner:
         def __init__(self):
             self.inner2=self.Inner()
         def show(self):
              print("this is inner class")

         class Inner:
            def show(self):
             print("this is an inner class of inner class")

outer=abc()
outer.show()
print()
g1=outer.inner1#object calling 
g1.show()
print()
g2=outer.inner1.inner2
g2.show()