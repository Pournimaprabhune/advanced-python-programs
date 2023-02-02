class color:
    def __init__(self):
     self.name="green"
     self.lg=self.lightgreen()
    def show(self):
        print("colour name :",self.name)
    class lightgreen:  
         def __init__(self):
            self.name="lightgreen"
            self.code=12345
         def display(self):
            print("colour name:",self.name)
            print("code :",self.code)

outer=color()
outer.show()
g=outer.lg
g.display()  
#outer.lg.display()  
   