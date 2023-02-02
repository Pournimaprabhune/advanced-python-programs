print("overriding __str__()method example in python")
class student:
     def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
     def __str__(self):
        return 'this is student object name:{} and rollno:{}'.format(self.name,self.rollno)
s1=student('anushree',100)
s2=student('samu',102)
print(s1)#it will print address of object s1 
print(s2)
