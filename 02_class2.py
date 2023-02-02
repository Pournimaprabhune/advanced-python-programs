#creating class
class employee:
    id=10
    name="anushree"
    def display(self):
        print("ID :",self.id,"name:",self.name)
a1=employee()
a1.display()

#deleting the property object
del a1.id
#deleting the object itself
#del a1
