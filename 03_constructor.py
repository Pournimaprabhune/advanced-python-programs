class employee:
        count=0
        def __init__(self,name,id):#parameterized constructor
              employee.count=employee.count+1
              self.id=id
              self.name=name
        def display(self):
                print("ID:%d  Name:%s"%(self.id,self.name))
   

emp1=employee("komal",101)#object passed paratmeter to constructor
emp2=employee("pournima",102)
emp3=employee("shaila",103)
emp1.display()
emp2.display() 
emp3.display()
print("the number of employee",employee.count)

class student:
     def __init__(self):
          print("this is non parameterized constructor ")
     def show(self,name):
            print("hello",name)

student1=student()
student1.show("john")

print("more than one constructor")
class student:
       def __init__(self):
         print("the first constructor")
       def  __init__(self):
           print("the second constructor")

st=student()